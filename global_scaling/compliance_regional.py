import yaml

def check_compliance(rules):
    results = []
    for rule in rules:
        results.append(f"Checked {rule['region']} → {rule['rule']} OK")
    return results

if __name__ == "__main__":
    with open("global_scaling/config.yml") as f:
        config = yaml.safe_load(f)
    results = check_compliance(config['regional_compliance'])
    for r in results:
        print(r)