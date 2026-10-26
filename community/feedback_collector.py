import pandas as pd
import datetime
import yaml

def log_feedback(user, feedback, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['feedback_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "feedback", "date"])
    new_entry = {"user": user, "feedback": feedback, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['feedback_storage'], index=False)
    print(f"Feedback logged from {user}: {feedback}")

if __name__ == "__main__":
    with open("community/config.yml") as f:
        config = yaml.safe_load(f)
    log_feedback("User123", "Love the automation services!", config)