import pandas as pd
import datetime
import yaml

def log_action(user, action, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['audit_log'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "action", "date"])
    new_entry = {"user": user, "action": action, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['audit_log'], index=False)
    print(f"Audit logged: {user} → {action}")

if __name__ == "__main__":
    with open("governance/config.yml") as f:
        config = yaml.safe_load(f)
    log_action("AdminUser", "Approved invoice", config)