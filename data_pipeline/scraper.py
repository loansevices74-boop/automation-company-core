import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml

def scrape_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = [item.text for item in soup.find_all('p')]
    return data

def scrape_json(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("data_pipeline/config.yml") as f:
        config = yaml.safe_load(f)

    all_data = []
    for source in config['sources']:
        if source['type'] == 'html':
            all_data.extend(scrape_html(source['url']))
        elif source['type'] == 'json':
            all_data.append(scrape_json(source['url']))

    df = pd.DataFrame(all_data)
    df.to_csv(config['report_output'], index=False)
    print("Data scraped and saved to report.")