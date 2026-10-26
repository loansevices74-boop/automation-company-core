import yaml

def list_marketplaces(config):
    for market in config['marketplaces']:
        print(f"Integrated with {market['name']}")

if __name__ == "__main__":
    with open("ecosystem/config.yml") as f:
        config = yaml.safe_load(f)
    list_marketplaces(config)