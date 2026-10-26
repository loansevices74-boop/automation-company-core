import yaml

def calculate_carbon(sources, factors):
    total_carbon = 0
    for src in sources:
        factor = next(f['factor'] for f in factors if f['source'] == src['name'])
        total_carbon += src['usage_kwh'] * factor
    print(f"Total carbon footprint: {total_carbon} kg CO2")
    return total_carbon

if __name__ == "__main__":
    with open("sustainability/config.yml") as f:
        config = yaml.safe_load(f)
    calculate_carbon(config['energy_sources'], config['carbon_factors'])