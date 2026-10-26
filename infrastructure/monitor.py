import requests
import yaml

def check_service(name, port):
    try:
        response = requests.get(f"http://localhost:{port}")
        if response.status_code == 200:
            print(f"{name} is running fine.")
        else:
            print(f"{name} returned status {response.status_code}.")
    except Exception:
        print(f"{name} is down!")

if __name__ == "__main__":
    with open("infrastructure/config.yml") as f:
        config = yaml.safe_load(f)
    for service in config['services']:
        check_service(service['name'], service['port'])