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
                 )->str:
    """
    Return a random question from the questions dataset.
    Type 1 questions are "Did you know"
    Type 2 questions are "Do you encourage this"
    """
    
    questions = load_data("../infra/data/questions.csv") # Can we load this only once when building the project?
    # If we want a specific question type
    if specific_type is not None:
        questions = questions[questions["Type"]==specific_type]
    # Random index to generate a random question
    idx = np.random.randint(0, len(questions), 1)
    return questions.loc[idx,"Question"].values[0]

# ------------------- Conversions ----------------------- #
def convert_GES_to_flights(ges: float)->float:
    """
    Convert a ges (en tonnes) into a number of flights (MTL) YUL->CDG (Paris)
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