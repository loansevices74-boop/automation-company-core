import yaml
import datetime

def get_scheduled_posts(config):
    today = datetime.date.today().weekday()
    posts = []
    for post in config['posts']:
        if post['schedule'] == "daily":
            posts.append(post['content'])
        elif post['schedule'] == "weekly" and today == 0:  # Monday
            posts.append(post['content'])
    return posts

if __name__ == "__main__":
    with open("social_media/config.yml") as f:
        config = yaml.safe_load(f)
    scheduled = get_scheduled_posts(config)
    print("Scheduled posts:", scheduled)