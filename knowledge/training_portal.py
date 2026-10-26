import pandas as pd
import datetime
import yaml

def add_training(course, description, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['training_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["course", "description", "date"])
    new_entry = {"course": course, "description": description, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['training_storage'], index=False)
    print(f"Training added: {course}")

if __name__ == "__main__":
    with open("knowledge/config.yml") as f:
        config = yaml.safe_load(f)
    add_training("Onboarding 101", "Introductory training for new clients.", config)