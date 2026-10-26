import shutil
import datetime
import os
import yaml

def backup_data(source, destination):
    today = datetime.date.today()
    backup_path = os.path.join(destination, f"backup_{today}")
    shutil.copytree(source, backup_path, dirs_exist_ok=True)
    print(f"Backup created at {backup_path}")

if __name__ == "__main__":
    with open("security/config.yml") as f:
        config = yaml.safe_load(f)
    os.makedirs(config['backup_storage'], exist_ok=True)
    backup_data("crm/", config['backup_storage'])
    backup_data("billing/", config['backup_storage'])