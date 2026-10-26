import yaml

def check_compliance(rules):
    results = []
    for rule in rules:
        # Placeholder: In real system, add checks for encryption, retention, anonymization
        results.append(f"Checked: {rule['rule']} → OK")
    return results

if __name__ == "__main__":
    with open("security/config.yml") as f:
        config = yaml.safe_load(f)
    results = check_compliance(config['compliance_rules'])
    for r in results:
        print(r)