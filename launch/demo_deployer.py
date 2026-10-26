import os
import yaml

def deploy_demo(env_path):
    os.makedirs(env_path, exist_ok=True)
    with open(os.path.join(env_path, "demo.txt"), "w") as f:
        f.write("Demo environment ready for clients.")
    print(f"Demo deployed at {env_path}")

if __name__ == "__main__":
    with open("launch/config.yml") as f:
        config = yaml.safe_load(f)
    deploy_demo(config['demo_environment'])