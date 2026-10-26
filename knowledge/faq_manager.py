import pandas as pd
import datetime
import yaml

def add_faq(question, answer, config):
    today = datetime.date.today()
    try:
        df = pd.read_csv(config['faq_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["question", "answer", "date"])
    new_entry = {"question": question, "answer": answer, "date": today}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['faq_storage'], index=False)
    print(f"FAQ added: {question} → {answer}")

if __name__ == "__main__":
    with open("knowledge/config.yml") as f:
        config = yaml.safe_load(f)
    add_faq("How do I reset my password?", "Go to settings → security → reset password.", config)