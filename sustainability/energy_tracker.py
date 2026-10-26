import yaml

def track_energy(sources):
    total = sum([src['usage_kwh'] for src in sources])
    print(f"Total energy usage: {total} kWh")
    return total

if __name__ == "__main__":
    with open("sustainability/config.yml") as f:
        config = yaml.safe_load(f)
    track_energy(config['energy_sources'])