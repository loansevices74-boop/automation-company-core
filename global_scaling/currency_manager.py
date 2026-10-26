import yaml

def convert_price(amount, currency):
    rates = {"USD": 1, "EUR": 0.9, "NGN": 1500, "GBP": 0.8}
    return amount * rates[currency]

if __name__ == "__main__":
    with open("global_scaling/config.yml") as f:
        config = yaml.safe_load(f)
    for currency in config['currencies']:
        print(f"Price in {currency}: {convert_price(50, currency)}")