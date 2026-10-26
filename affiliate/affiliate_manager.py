import pandas as pd
import datetime
import yaml

def add_affiliate(name, email, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['affiliate_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["name", "email", "join_date"])
    new_entry = {"name": name, "email": email, "join_date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['affiliate_storage'], index=False)
    print(f"Affiliate {name} added.")

if __name__ == "__main__":
    with open("affiliate/config.yml") as f:
        config = yaml.safe_load(f)
    add_affiliate("PartnerX", "partner@example.com", config)