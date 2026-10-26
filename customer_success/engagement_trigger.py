import yaml

def trigger_engagement(condition, actions):
    for act in actions:
        if act['condition'] == condition:
            print(f"Engagement triggered: {act['action']}")

if __name__ == "__main__":
    with open("customer_success/config.yml") as f:
        config = yaml.safe_load(f)
    trigger_engagement("low_health", config['engagement_actions'])