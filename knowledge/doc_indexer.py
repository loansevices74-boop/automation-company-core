import pandas as pd
import yaml

def index_doc(title, path, config):
    try:
        df = pd.read_csv(config['docs_storage'])
    except FileNotFoundError:
        df = pd.DataFrame(columns=["title", "path"])
    new_entry = {"title": title, "path": path}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(config['docs_storage'], index=False)
    print(f"Document indexed: {title}")

if __name__ == "__main__":
    with open("knowledge/config.yml") as f:
        config = yaml.safe_load(f)
    index_doc("CRM Guide", "docs/crm_guide.pdf", config)