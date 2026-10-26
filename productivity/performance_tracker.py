import pandas as pd
import datetime
import yaml

def log_performance(user, metric, value, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['performance_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "metric", "value", "date"])
    new_entry = {"user": user, "metric": metric, "value": value, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['performance_storage'], index=False)
    print(f"Performance logged: {user} → {metric}: {value}")

if __name__ == "__main__":
    with open("productivity/config.yml") as f:
        config = yaml.safe_load(f)
    log_performance("TeamMember1", "Tasks Completed", 5, config)