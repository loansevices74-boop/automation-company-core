import pandas as pd
import datetime
import yaml

def onboard_client(client_name, plan, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["client", "plan", "start_date"])
    new_entry = {"client": client_name, "plan": plan, "start_date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['storage'], index=False)
    print(f"Client {client_name} onboarded with {plan} plan.")

if __name__ == "__main__":
    with open("subscriptions/config.yml") as f:
        config = yaml.safe_load(f)
    onboard_client("ClientA", "Free", config)