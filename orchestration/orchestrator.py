import subprocess
import yaml

def run_service(service):
    print(f"Running {service['name']}...")
    try:
        subprocess.run(["python", f"{service['path']}"], check=True)
    except Exception as e:
        print(f"Error running {service['name']}: {e}")

if __name__ == "__main__":
    with open("orchestration/config.yml") as f:
        config = yaml.safe_load(f)
    for service in config['services']:
        run_service(service)