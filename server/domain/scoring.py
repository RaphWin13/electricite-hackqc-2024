import pandas as pd
import numpy as np
from datetime import datetime
import pytz

from datetime import timedelta

# Get Quebec Last 24H Conso in KWh
def getQuebecLast24HConso(dataPath = r"../infra/data/2022-sources-electricite-quebec.csv") -> float:
  elecHistory = pd.read_csv(dataPath)

  now = (datetime.now(pytz.timezone('America/Toronto'))+ timedelta(hours=-25)).strftime("2022-%m-%d %H:30")
  startIdx = elecHistory[elecHistory["Date"]==now].index[0]

  return elecHistory.iloc[startIdx:startIdx+24]["Total "].sum()*1000

#Get building ratio
def getRatio()->pd.Series:
  return pd.read_json(r"../infra/data/ratio_edifice_electricite.json")["ratio"]

# Get building Last 24H conso in KWh
def getBatLast24HConso()->list[float]:
   batConso = getRatio()*getQuebecLast24HConso() 
   epsilon = np.random.normal(loc = -0.1, scale=0.2, size= len(batConso)) #A jouer dessus pour jouer sur le epsilon ajouter pour les résultats
   return list(batConso + epsilon*batConso)

# Get building Last year's month conso in KWh
def getQuebecLastYearMonthConsumptions(dataPath = r"../infra/data/2021-sources-electricite-quebec.xlsx")->pd.Series:
  lastYearConso = pd.read_excel(dataPath)
  nowMonth = datetime.now(pytz.timezone('America/Toronto')).month
  LastYearMonthsConsumptions = 0
  for i in range(len(lastYearConso)):
    if lastYearConso["Date"][i].month == nowMonth: 
      LastYearMonthsConsumptions += lastYearConso["Total "][i]
  return LastYearMonthsConsumptions*1000
# Get building Last year's month conso in KWh

def getBatLastYearMonthConsumptions(dataPath = r"../infra/data/2021-sources-electricite-quebec.xlsx")->pd.Series:
  return getRatio()*getQuebecLastYearMonthConsumptions()

# Get day average of building Last year's month conso in KWh
def getDayAverageQuebecLastYearMonthConsumptions()->pd.Series:
  return getQuebecLastYearMonthConsumptions()/31 # Pour la demo on est en Mars donc 31 jours mais à refaire pour que ça soit plus clean

# Get day average of building Last year's month conso in KWh
def getDayAverageBatLastYearMonthConsumptions()->pd.Series:
  return getBatLastYearMonthConsumptions()/31 # Pour la demo on est en Mars donc 31 jours mais à refaire pour que ça soit plus clean
  
# Compute numeric score
def getScoreNumeric()->pd.Series:
  batsAverageLastYearDay = getDayAverageBatLastYearMonthConsumptions()
  batLast24HConso = getBatLast24HConso()
  return (batLast24HConso - batsAverageLastYearDay)/batsAverageLastYearDay

# Compute letter score
def getScoreLetter()->list[str]:
  numScores = getScoreNumeric()
  letterScores = []
  for i in range(len(numScores)):
    if numScores[i] <= -0.15: letterScores.append("A")
    elif numScores[i] <= -0.05: letterScores.append("B")
    elif numScores[i] <= 0: letterScores.append("C")
    elif numScores[i] <= 0.10: letterScores.append("D")
    else : letterScores.append("E")
  return letterScores
  
# Get JsonFormat for building name position and numeric score
def getJsonPostionAndScoreNumeric()-> str:
  batData = pd.read_json(r"../infra/data/ratio_edifice_electricite.json")
  batData["score"] = getScoreNumeric()
  return batData[["Nom","Latitude","Longitude","score"]].to_json(orient="index")

# Get JsonFormat for building name position and letter score
def getJsonPostionAndScoreLetter()-> str:
  batData = pd.read_json(r"../infra/data/ratio_edifice_electricite.json")
  batData["score"] = getScoreLetter()
  return batData[["Nom","Latitude","Longitude","score"]].to_json(orient="index")

# Get JsonFormat for top 3 building with name position and numeric score
def getJsonPodiumScore()->str:
  batData = pd.read_json(r"../infra/data/ratio_edifice_electricite.json")
  batData["score"] = getScoreNumeric()
  return batData[["Nom","Latitude","Longitude","score"]].sort_values(by=['score']).iloc[:3].reset_index(drop=True).to_json(orient="index")

# Get JsonFormat for top 3 building with name position and numeric score
def getJsonPodiumConso()->str:
  batData = pd.read_json(r"../infra/data/ratio_edifice_electricite.json")
  batData["score"] = getScoreNumeric()*getDayAverageBatLastYearMonthConsumptions() * (365*3.5/1500000)
  return batData[["Nom","Latitude","Longitude","score"]].sort_values(by=['score']).iloc[:3].reset_index(drop=True).to_json(orient="index")

def create_ratio_file()->None:
  bats = pd.read_csv("/content/edifices_GES_electricite.csv")
  consoQuebecJournalier2022 = pd.read_csv("/content/2022-sources-electricite-quebec.csv")
  total2021KWh = consoQuebecJournalier2022["Total "].sum()*1000
  bats["ratio"]= bats["Electricite"]/total2021KWh
  bats.to_json("./ratio_edifice_electricite.json")