import os
import datetime
import yaml

def generate_invoice(client_name, service, amount, config):
    today = datetime.date.today()
    invoice_id = f"INV-{today.strftime('%Y%m%d')}-{client_name}"
    invoice_text = f"""
    Invoice ID: {invoice_id}
    Company: {config['company_name']}
    Client: {client_name}
    Service: {service}
    Amount: {amount} {config['currency']}
    Date: {today}
    """
    output_path = os.path.join(config['invoice_output'], f"{invoice_id}.txt")
    os.makedirs(config['invoice_output'], exist_ok=True)
    with open(output_path, "w") as f:
        f.write(invoice_text)
    print(f"Invoice generated: {output_path}")

if __name__ == "__main__":
    with open("billing/config.yml") as f:
        config = yaml.safe_load(f)
    generate_invoice("ClientX", "Automation Workflow Setup", config['default_rate'], config)