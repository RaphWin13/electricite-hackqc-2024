import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pytz
import requests
from .address_converter import convert_to_lat_long

EDIFICES_FILE = r"infra/data/consommation-energetique-tous.csv"
RATIO_FILE = r"infra/data/ratio_edifice_electricite.json"
SOURCES_2022_FILE = r"infra/data/download/2022-sources-electricite-quebec.csv"
SOURCES_2021_FILE = r"infra/data/download/2021-sources-electricite-quebec.csv"
CO2_G_AIRPLANE_TRAVEL_MTL_PARIS = 1000000
CO2_G_AIRPLANE_TRAVEL_MTL_NY = 100000
CO2_G_PAR_KWH = 34.5
CO2_G_PAR_KM_AUTO = 82
DISTANCE_QC_MTL_KM = 233
IDX_BATIMENTS_QUARTIER = [66, 89, 125, 186, 187, 188]
# All consumption in KWh

# Load Data de Laurence
def load_csv(string_path:str, sep:str=",", parse_dates=None)->pd.DataFrame:
    """
    Load the data from a relative path
    """
    with open(string_path, "r", encoding="utf-8") as f:
        content = pd.read_csv(f, sep=sep, parse_dates=parse_dates, encoding="utf-8")
    return content 

def create_building_ratio_file():
    buildingConsumption = load_csv(EDIFICES_FILE, sep=';')
    buildingPositions = buildingConsumption.apply(lambda row: convert_to_lat_long(row['Adresse_civique'], row['Arrondissement']), axis=1)
    buildingConsumption['Latitude'] = buildingPositions.apply(lambda x: x['lat'])
    buildingConsumption['Longitude'] = buildingPositions.apply(lambda x: x['lng'])

    lastYearDailyQuebecConsumption = load_csv(SOURCES_2022_FILE, parse_dates=["Date"])
    totalLastYearKWh = lastYearDailyQuebecConsumption["Total "].sum() * 1000
    buildingConsumption["ratio"] = buildingConsumption["Electricite"] / totalLastYearKWh

    buildingConsumptionWithRatioAndPosition = buildingConsumption[["Nom_batiment", "Superficie", "Electricite", "Emissions_GES", "Latitude", "Longitude", "ratio"]].rename(columns={"Nom_batiment": "Nom"})
    buildingConsumptionWithRatioAndPosition.to_json(RATIO_FILE)

def get_last_24h_consumption(dataPath = SOURCES_2022_FILE) -> float:
  elecHistory = pd.read_csv(dataPath)

  now = (datetime.now(pytz.timezone('America/Toronto')) + timedelta(hours=-25)).strftime("2022-%m-%d %H:30")
  startIdx = elecHistory[elecHistory["Date"]==now].index[0]

  return elecHistory.iloc[startIdx:startIdx+24]["Total "].sum()*1000

def get_building_ratio(idx: list[int] = None)->pd.Series:
  ratios_json = pd.read_json(RATIO_FILE)
  if idx is None:
    return ratios_json["ratio"]
  
  return ratios_json["ratio"].iloc[idx]

def get_randomized_24h_consumption()->list[float]:
  consumption = get_building_ratio()*get_last_24h_consumption() 
  epsilon = np.random.normal(loc = -0.1, scale=0.2, size= len(consumption)) #A jouer dessus pour jouer sur le epsilon ajouter pour les résultats
  return list(consumption + epsilon*consumption)

random_consumption = get_randomized_24h_consumption()

def get_last_year_monthly_consumption(dataPath = SOURCES_2021_FILE)->pd.Series:
  lastYearConsumption = load_csv(dataPath, parse_dates=["Date"])
  nowMonth = datetime.now(pytz.timezone('America/Toronto')).month
  LastYearMonthsConsumptions = 0
  for i in range(len(lastYearConsumption)):
    if lastYearConsumption["Date"][i].month == nowMonth: 
      LastYearMonthsConsumptions += lastYearConsumption["Total "][i]
  return LastYearMonthsConsumptions*1000

def get_weighed_daily_average_of_last_year_monthly_consumption(idx: list[int] = None)->pd.Series:
  return get_building_ratio(idx)*get_last_year_monthly_consumption()/31 # Pour la demo on est en Mars donc 31 jours mais à refaire pour que ça soit plus clean
  
def compute_numeric_score(idx: list[int] = None)->pd.Series:
  averageLastYearDay = get_weighed_daily_average_of_last_year_monthly_consumption(idx)
  last24HConsumption = random_consumption if idx is None else [random_consumption[i] for i in idx]
  return (last24HConsumption - averageLastYearDay)/averageLastYearDay

def compute_letter_score()->list[str]:
  num_scores = compute_numeric_score()
  letter_scores = []
  for i in range(len(num_scores)):
    if num_scores[i] <= -0.15: letter_scores.append("A")
    elif num_scores[i] <= -0.05: letter_scores.append("B")
    elif num_scores[i] <= 0: letter_scores.append("C")
    elif num_scores[i] <= 0.10: letter_scores.append("D")
    else : letter_scores.append("E")
  return letter_scores
  
# Get JsonFormat for building name position and numeric score
def get_json_postion_and_numeric_score()-> str:
  batData = pd.read_json(RATIO_FILE)
  batData["score"] = compute_numeric_score()
  return batData[["Nom","Latitude","Longitude","score"]].to_json(orient="index")

# Get JsonFormat for building name position and letter score
def get_json_position_and_score_letter()-> str:
  batData = pd.read_json(RATIO_FILE)
  batData["score"] = compute_letter_score()
  return batData[["Nom","Latitude","Longitude","score"]].to_json(orient="index", force_ascii=False)

# Get JsonFormat for top 3 building with name position and numeric score
def get_json_podium_score()->str:
  batData = pd.read_json(RATIO_FILE)
  num_score = compute_numeric_score(IDX_BATIMENTS_QUARTIER)
  batData["score"] = num_score
  batData["eq_airplane"] = num_score*get_weighed_daily_average_of_last_year_monthly_consumption() * (CO2_G_PAR_KWH/CO2_G_AIRPLANE_TRAVEL_MTL_NY)
  return batData[["Nom","Latitude","Longitude","score", "eq_airplane"]].sort_values(by=['score']).iloc[:3].reset_index(drop=True).to_json(orient="index", force_ascii=False)
