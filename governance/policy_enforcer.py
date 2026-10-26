import yaml

def enforce_policies(policies):
    for policy in policies:
        print(f"Policy enforced: {policy['name']} → {policy['rule']}")

if __name__ == "__main__":
    with open("governance/config.yml") as f:
        config = yaml.safe_load(f)
    enforce_policies(config['policies'])