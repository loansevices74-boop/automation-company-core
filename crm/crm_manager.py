import pandas as pd
import datetime
import yaml

def add_client(client_name, service, status, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['crm_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["client", "service", "status", "last_contact"])
    new_entry = {"client": client_name, "service": service, "status": status, "last_contact": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['crm_storage'], index=False)
    print(f"Client {client_name} added to CRM.")

def update_status(client_name, status, config):
    df = pd.read_csv(config['crm_storage'])
    df.loc[df['client'] == client_name, 'status'] = status
    df.to_csv(config['crm_storage'], index=False)
    print(f"Client {client_name} status updated to {status}.")

if __name__ == "__main__":
    with open("crm/config.yml") as f:
        config = yaml.safe_load(f)
    add_client("ClientZ", "Data Reporting Workflow", "active", config)
    update_status("ClientX", "inactive", config)