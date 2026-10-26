import pandas as pd
import yaml

def recommend_action(client_data, rules):
    recommendations = []
    for rule in rules:
        if rule['condition'] in client_data:
            recommendations.append(rule['action'])
    return recommendations

if __name__ == "__main__":
    with open("personalization/config.yml") as f:
        config = yaml.safe_load(f)
    client_data = ["active_clients > 10", "plan == 'Premium'"]
    recs = recommend_action(client_data, config['rules'])
    print("Recommendations:", recs)