import requests
import yaml

def send_slack_message(content, config):
    url = config['api_url']
    headers = {"Authorization": f"Bearer {config['token']}"}
    data = {"channel": "#general", "text": content}
    response = requests.post(url, headers=headers, data=data)
    print("Slack response:", response.status_code)

def create_trello_card(title, config):
    url = config['api_url']
    params = {"key": config['key'], "token": config['token'], "idList": "your_list_id", "name": title}
    response = requests.post(url, params=params)
    print("Trello response:", response.status_code)

if __name__ == "__main__":
    with open("ecosystem/config.yml") as f:
        config = yaml.safe_load(f)
    send_slack_message("Automation update: new client onboarded!", config['integrations'][0])
    create_trello_card("Automation Task: Client Setup", config['integrations'][1])