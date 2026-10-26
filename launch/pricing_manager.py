import yaml

def show_pricing(config):
    for tier in config['pricing_tiers']:
        print(f"{tier['name']} Plan: ${tier['price']} → Features: {', '.join(tier['features'])}")

if __name__ == "__main__":
    with open("launch/config.yml") as f:
        config = yaml.safe_load(f)
    show_pricing(config)