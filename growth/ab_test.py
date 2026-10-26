import random
import yaml

def run_ab_test(test):
    chosen = random.choice([test['variant_a'], test['variant_b']])
    print(f"A/B Test '{test['name']}': Showing → {chosen}")
    return chosen

if __name__ == "__main__":
    with open("growth/config.yml") as f:
        config = yaml.safe_load(f)
    for test in config['tests']:
        run_ab_test(test)