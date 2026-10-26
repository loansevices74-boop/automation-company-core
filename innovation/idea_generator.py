import random
import yaml

def generate_idea(ideas):
    idea = random.choice(ideas)
    print(f"New innovation idea: {idea}")
    return idea

if __name__ == "__main__":
    with open("innovation/config.yml") as f:
        config = yaml.safe_load(f)
    generate_idea(config['ideas'])