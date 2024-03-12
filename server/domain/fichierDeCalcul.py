import pandas as pd
import numpy as np

def load_data(string_path:str, sep:str=";"
              )->pd.DataFrame:
    """
    Load the data from a relative path
    """
    with open(string_path, "r") as f:
        content = pd.read_csv(f, sep=sep)
    return content

# --------------- Questions --------------------------#
def get_question(specific_type:int = None
                 )->tuple[str, float]:
    """
    Return a random question from the questions dataset.
    Type 1 questions are "Did you know"
    Type 2 questions are "Do you encourage this"
    """
    
    questions = load_data("infra/data/questions.csv") # Can we load this only once when building the project?
    # If we want a specific question type
    if specific_type is not None:
        questions = questions[questions["Type"]==specific_type]
    # Random index to generate a random question
    idx = np.random.randint(0, len(questions), 1)
    quest = questions.loc[idx,"Question"].values[0]
    type = questions.loc[idx,"Type"].values[0]
    return quest, str(type) # Change les données str

# ------------------- Conversions ----------------------- #
def convert_GES_to_flights(ges: float)->float:
    """
    Convert a GES (en tonnes) into a number of flights (MTL) YUL->CDG (Paris)
    """
    # 1.5 tonnes per flight YUL -> CDG
    # https://calculator.carbonfootprint.com/calculator.aspx?tab=3 
    if ges % 1.5 == 0:
        return int(ges / 1.5)
    else:
        return np.round(ges / 1.5, 1)

def convert_energy_to_ges():
    """
    Convert an energy consumption into a ges emission
    """
    # 34.5 g per kWh of energy
    # https://www.hydroquebec.com/developpement-durable/documentation-specialisee/taux-emission-ges.html#:~:text=Pour%20calculer%20ces%20derni%C3%A8res%20%C3%A9missions,l'%C3%A9lectricit%C3%A9%20achet%C3%A9e%20et%20import%C3%A9e.
    pass # Can use the ges column in the data

# ------------------ Consumption per map sector -------------- #
def consumption_per_sector():
    """
    Suppose the data has a new column which is the energy consumption
    per hour, then we aggregate that per sector. TODO : Adapt the column name to sum
    """
    data = load_data("../infra/data/consommation-energetique-tous.csv")
    aggregated_data = pd.DataFrame(columns=["Arrondissement", "Electricite","Emissions_GES"])
    # Loop over all sections of the map
    for g, sector in data.groupby("Arrondissement"):
        aggregated_data.loc[len(aggregated_data.index)] = [g, sector["Electricite"].sum(), sector["Emissions_GES"].sum()]
        # TODO : Extract lat-long square coordinates (min and max in both directions)
    print(aggregated_data)
#consumption_per_sector()

# En temps réel (recalculer)
# - Ratio pour avoir la valeur par bâtisse le jour
# - Prendre ces valeurs là pour aggréger
# - Extraire min et max pour polygones
# -- Map, connecter les questions
# - coordonnées arrondissements