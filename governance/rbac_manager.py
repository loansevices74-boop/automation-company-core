import yaml

def check_permission(role, permission, roles):
    role_data = next(r for r in roles if r['name'] == role)
    if permission in role_data['permissions']:
        print(f"Permission granted: {role} → {permission}")
    else:
        print(f"Permission denied: {role} → {permission}")

if __name__ == "__main__":
    with open("governance/config.yml") as f:
        config = yaml.safe_load(f)
    check_permission("Manager", "approve_billing", config['roles'])