import yaml

def log_innovation(idea, result, config):
    with open(config['innovation_log'], "a") as f:
        f.write(f"Idea: {idea} → Result: {result}\n")
    print(f"Innovation logged: {idea} → {result}")

if __name__ == "__main__":
    with open("innovation/config.yml") as f:
        config = yaml.safe_load(f)
    log_innovation("Voice-enabled chatbot", "Success", config)