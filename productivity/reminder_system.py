import pandas as pd
import datetime
import yaml

def add_reminder(user, reminder, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['reminders_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "reminder", "date"])
    new_entry = {"user": user, "reminder": reminder, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['reminders_storage'], index=False)
    print(f"Reminder set: {user} → {reminder}")

if __name__ == "__main__":
    with open("productivity/config.yml") as f:
        config = yaml.safe_load(f)
    add_reminder("TeamMember1", "Submit report by Friday", config)