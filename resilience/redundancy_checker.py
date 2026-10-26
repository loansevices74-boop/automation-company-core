import yaml

def check_redundancy(services):
    for svc in services:
        if svc['replicas'] >= 2:
            print(f"{svc['service']} redundancy OK ({svc['replicas']} replicas).")
        else:
            print(f"{svc['service']} redundancy insufficient!")

if __name__ == "__main__":
    with open("resilience/config.yml") as f:
        config = yaml.safe_load(f)
    check_redundancy(config['redundancy_checks'])