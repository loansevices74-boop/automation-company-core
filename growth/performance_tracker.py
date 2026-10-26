import pandas as pd
import datetime
import yaml

def log_performance(test_name, variant, result, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['performance_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["test", "variant", "result", "date"])
    new_entry = {"test": test_name, "variant": variant, "result": result, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['performance_storage'], index=False)
    print(f"Performance logged: {test_name} → {variant} → {result}")

if __name__ == "__main__":
    with open("growth/config.yml") as f:
        config = yaml.safe_load(f)
    log_performance("Landing Page Headline", "Variant A", "Conversion", config)