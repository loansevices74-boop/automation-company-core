import pandas as pd
import datetime
import yaml

def test_prototype(idea, config):
    today = datetime.date.today()
    result = "Success" if "AI" in idea else "Needs improvement"
    try:
        df = pd.read_csv(config['prototype_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["idea", "result", "date"])
    new_entry = {"idea": idea, "result": result, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['prototype_storage'], index=False)
    print(f"Prototype tested: {idea} → {result}")

if __name__ == "__main__":
    with open("innovation/config.yml") as f:
        config = yaml.safe_load(f)
    test_prototype("AI-driven customer sentiment analysis", config)