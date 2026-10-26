import yaml
import requests

def post_to_mastodon(content, config):
    url = f"{config['api_url']}/api/v1/statuses"
    headers = {"Authorization": f"Bearer {config['access_token']}"}
    data = {"status": content}
    response = requests.post(url, headers=headers, data=data)
    print("Mastodon response:", response.status_code)

if __name__ == "__main__":
    with open("social_media/config.yml") as f:
        config = yaml.safe_load(f)
    posts = ["Automation Tip of the Day: Save time with workflows!"]
    for post in posts:
        post_to_mastodon(post, config['platforms'][1])