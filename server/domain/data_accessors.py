import pandas as pd
import numpy as np
from pathlib import Path


def load_data(string_path:str, sep:str=";"
              )->pd.DataFrame:
    """
    Load the data from a relative path
    """
    with open(string_path, "r", encoding="utf-8") as f:
        content = pd.read_csv(f, sep=sep, encoding="utf-8")
    return content

# --------------- Questions --------------------------#
def get_question(specific_type:int = None
                 )->tuple[str, float]:
    """
    Return a random question from the questions dataset.
    Type 1 questions are "Did you know"
    Type 2 questions are "Do you encourage this"
    """
    
    questions = load_data("infra/data/questions.csv")
    # If we want a specific question type
    if specific_type is not None:
        questions = questions[questions["Type"]==specific_type]
    # Random index to generate a random question
    id = np.random.randint(0, len(questions), 1)[0]
    quest = questions.loc[id,"Question"]
    type = questions.loc[id,"Type"]
    return quest, str(type), str(id)

# ------------------- Fun facts ------------------------ #
def get_fun_fact()->tuple[str, float]:
    """
    Return a random fun fact.
    """
    funfact = load_data("infra/data/fun_facts.csv")
    
    # Random index to generate a random question
    idx = np.random.randint(0, len(funfact), 1)
    fact = funfact.loc[idx,"valeur"].values[0]
    equiv = funfact.loc[idx,"equivalence"].values[0]
    return fact, equiv

# ------------------- log answer data --------------------- #
def log_answer(question_id, answer):
    print(question_id, answer)
    # Create file if it does not exist
    if not Path("infra/data/answers.csv").exists():
        questions = pd.read_csv("infra/data/questions.csv")
        num_questions = questions.shape[0]
        new_df = pd.DataFrame({"ID":range(num_questions), "0":np.repeat(0, num_questions), "1":np.repeat(0, num_questions)})
        new_df.to_csv("infra/data/answers.csv", index=False)

    # Load the values of the question
    question_info = pd.read_csv("infra/data/answers.csv")

    # Save the answer to the cumulative sum corresponding (1 : yes, 0 : no)
    question_info.loc[question_info["ID"] == int(question_id), str(answer)] += 1

    # Save update dataframe
    question_info.to_csv("infra/data/answers.csv", index=False)
    return "Logging successful"

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
