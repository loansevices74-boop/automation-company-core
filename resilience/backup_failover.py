import requests
import yaml

def check_failover(servers):
    for srv in servers:
        try:
            response = requests.get(srv['url'])
            if response.status_code == 200:
                print(f"{srv['name']} server is healthy.")
            else:
                print(f"{srv['name']} server issue: {response.status_code}")
        except Exception:
            print(f"{srv['name']} server unreachable!")

if __name__ == "__main__":
    with open("resilience/config.yml") as f:
        config = yaml.safe_load(f)
    check_failover(config['failover_servers'])