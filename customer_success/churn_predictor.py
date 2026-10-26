import yaml

def predict_churn(score, threshold):
    if score < threshold:
        print("Churn risk detected!")
        return True
    else:
        print("Client stable.")
        return False

if __name__ == "__main__":
    with open("customer_success/config.yml") as f:
        config = yaml.safe_load(f)
    predict_churn(0.4, config['churn_threshold'])