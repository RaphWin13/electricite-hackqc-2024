import pandas as pd
import numpy as np
from datetime import datetime


#Get actual consumption in KWh
def getActualConso()-> float:
  consoData = pd.read_json("..\infra\data\production.json") # A récupérer sur ce site : https://www.hydroquebec.com/data/documents-donnees/donnees-ouvertes/json/production.json
  lastAvailableData = consoData["indexDonneePlusRecent"][0]
  return consoData["details"][lastAvailableData]["valeurs"]["total"]*1000

#Get ratios of each building
def getRatio()-> pd.Series:
  return pd.read_json("..\infra\data\consoBatRatio.json")["ratio"]

#Get actual consumption of each building in KWh
def getBatActualConsumptions()-> float:
   batConso = getRatio()*getActualConso() 
   epsilon = np.random.normal(0, 0.1, len(batConso))
   return list(batConso + epsilon*batConso)

# Generate 2022's 3 months consumption in KWh
def getBatLastYear3MonthsConsumptions() -> float:
  consoQuebecJournalier2022 = pd.read_csv("..\infra\data\2022-sources-electricite-quebec.csv")
  actualMonth = datetime.now().month
  if actualMonth > 1 : startMonth = str(actualMonth -1)
  else : startMonth = str(1)

  if len(startMonth) == 1:
    startMonth = "0"+startMonth
  
  startIdx = consoQuebecJournalier2022[consoQuebecJournalier2022["Date"] == "2022-"+startMonth+"-01 00:30"].index[0]
  return consoQuebecJournalier2022.iloc[startIdx: min(len(consoQuebecJournalier2022),startIdx+90)]["Total "]*1000

def getHourAverageConsumptionOfLastYear3Months()-> float:
  return np.mean(getBatLastYear3MonthsConsumptions())
  

def getScoreNumeric()-> pd.Series:
  previousAverageBatConsumptionPerHour = getHourAverageConsumptionOfLastYear3Months() * getRatio()
  return (getBatActualConsumptions() - previousAverageBatConsumptionPerHour)/previousAverageBatConsumptionPerHour

def getScoreLetter()-> list[str]:
  numScores = getScoreNumeric()
  letterScores = []
  for i in range(len(numScores)):
    if numScores[i] <= -0.3: letterScores.append("A")
    elif numScores[i] <= -0.10: letterScores.append("B")
    elif numScores[i] <= 0.02: letterScores.append("C")
    elif numScores[i] <= 0.15: letterScores.append("D")
    else : letterScores.append("E")