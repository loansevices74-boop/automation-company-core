import pandas as pd
import datetime
import yaml

def log_payment(client_name, amount, config):
    today = datetime.date.today()
    payment = {"client": client_name, "amount": amount, "date": today}
    try:
        df = pd.read_csv(config['payment_log'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["client", "amount", "date"])
    df = pd.concat([df, pd.DataFrame([payment])], ignore_index=True)
    df.to_csv(config['payment_log'], index=False)
    print(f"Payment logged for {client_name}: {amount} {config['currency']}")

if __name__ == "__main__":
    with open("billing/config.yml") as f:
        config = yaml.safe_load(f)
    log_payment("ClientX", 100, config)