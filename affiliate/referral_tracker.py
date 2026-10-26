import pandas as pd
import datetime
import yaml

def log_referral(affiliate_name, client_name, amount, config):
    today = datetime.date.today()
    commission = amount * config['commission_rate']
    try:
        df = pd.read_csv(config['referral_log'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["affiliate", "client", "amount", "commission", "date"])
    new_entry = {"affiliate": affiliate_name, "client": client_name,
                 "amount": amount, "commission": commission, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['referral_log'], index=False)
    print(f"Referral logged: {affiliate_name} → {client_name}, commission {commission}")

if __name__ == "__main__":
    with open("affiliate/config.yml") as f:
        config = yaml.safe_load(f)
    log_referral("PartnerX", "ClientY", 200, config)