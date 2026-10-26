import yaml

def run_recovery(plan):
    for step in plan:
        print(f"Executing recovery step: {step['step']}")

if __name__ == "__main__":
    with open("resilience/config.yml") as f:
        config = yaml.safe_load(f)
    run_recovery(config['disaster_recovery_plan'])