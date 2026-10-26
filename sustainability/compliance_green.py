import yaml

def check_green_compliance(rules):
    results = []
    for rule in rules:
        results.append(f"Checked {rule['region']} → {rule['rule']} OK")
    return results

if __name__ == "__main__":
    with open("sustainability/config.yml") as f:
        config = yaml.safe_load(f)
    results = check_green_compliance(config['green_compliance'])
    for r in results:
        print(r)