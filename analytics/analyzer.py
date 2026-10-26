import pandas as pd
import yaml

def analyze_clients(crm_path):
    df = pd.read_csv(crm_path)
    active_clients = df[df['status'] == 'active']
    return f"Active clients: {len(active_clients)}"

def analyze_payments(billing_path):
    df = pd.read_csv(billing_path)
    total_revenue = df['amount'].sum()
    return f"Total revenue: ${total_revenue}"

if __name__ == "__main__":
    with open("analytics/config.yml") as f:
        config = yaml.safe_load(f)
    client_summary = analyze_clients(config['sources'][0]['crm'])
    payment_summary = analyze_payments(config['sources'][1]['billing'])
    print(client_summary)
    print(payment_summary)