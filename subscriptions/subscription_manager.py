import pandas as pd
import yaml

def upgrade_plan(client_name, new_plan, config):
    df = pd.read_csv(config['storage'])
    df.loc[df['client'] == client_name, 'plan'] = new_plan
    df.to_csv(config['storage'], index=False)
    print(f"Client {client_name} upgraded to {new_plan} plan.")

if __name__ == "__main__":
    with open("subscriptions/config.yml") as f:
        config = yaml.safe_load(f)
    upgrade_plan("ClientA", "Premium", config)