import yaml

def calculate_health(metrics):
    score = sum([m['weight'] for m in metrics])  # placeholder logic
    print(f"Client health score: {score}")
    return score

if __name__ == "__main__":
    with open("customer_success/config.yml") as f:
        config = yaml.safe_load(f)
    calculate_health(config['health_metrics'])