import requests
import yaml

def post_message(content, config):
    url = f"{config['api_url']}/posts.json"
    headers = {"Api-Key": config['api_key'], "Api-Username": config['api_user']}
    data = {"title": "Community Update", "raw": content}
    response = requests.post(url, headers=headers, data=data)
    print("Forum post response:", response.status_code)

if __name__ == "__main__":
    with open("community/config.yml") as f:
        config = yaml.safe_load(f)
    post_message("Welcome to our automation community! Share your ideas here.", config['platforms'][0])