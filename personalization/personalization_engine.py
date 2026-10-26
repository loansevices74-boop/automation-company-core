import pandas as pd
import datetime
import yaml

def log_recommendations(client, recs, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['output'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["client", "recommendation", "date"])
    for rec in recs:
        new_entry = {"client": client, "recommendation": rec, "date": today}
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['output'], index=False)
    print(f"Personalization logged for {client}: {recs}")

if __name__ == "__main__":
    with open("personalization/config.yml") as f:
        config = yaml.safe_load(f)
    recs = ["Show advanced analytics", "Send productivity tips"]
    log_recommendations("ClientX", recs, config)