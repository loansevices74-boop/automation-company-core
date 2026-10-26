import yaml

def deploy_service(service, provider):
    print(f"Deploying {service['name']} to {provider} on port {service['port']}...")

if __name__ == "__main__":
    with open("infrastructure/config.yml") as f:
        config = yaml.safe_load(f)
    for service in config['services']:
        deploy_service(service, config['cloud_provider'])