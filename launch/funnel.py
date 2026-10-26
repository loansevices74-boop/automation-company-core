import pandas as pd
import datetime
import yaml

def log_funnel_step(client, step, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['funnel_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["client", "step", "date"])
    new_entry = {"client": client, "step": step, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['funnel_storage'], index=False)
    print(f"Funnel step logged: {client} → {step}")

if __name__ == "__main__":
    with open("launch/config.yml") as f:
        config = yaml.safe_load(f)
    log_funnel_step("ClientX", "Signed up for demo", config)