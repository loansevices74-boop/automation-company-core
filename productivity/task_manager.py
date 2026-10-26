import pandas as pd
import datetime
import yaml

def add_task(user, task, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['tasks_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "task", "date"])
    new_entry = {"user": user, "task": task, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['tasks_storage'], index=False)
    print(f"Task added: {user} → {task}")

if __name__ == "__main__":
    with open("productivity/config.yml") as f:
        config = yaml.safe_load(f)
    add_task("TeamMember1", "Prepare weekly report", config)