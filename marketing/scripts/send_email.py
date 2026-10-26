import smtplib
from email.mime.text import MIMEText
import yaml

def send_email(recipient, subject, body, config):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config['default_sender']
    msg['To'] = recipient

    with smtplib.SMTP(config['smtp_host'], config['smtp_port']) as server:
        server.starttls()
        server.login(config['smtp_user'], config['smtp_pass'])
        server.sendmail(config['default_sender'], [recipient], msg.as_string())

if __name__ == "__main__":
    with open("marketing/config.yml") as f:
        config = yaml.safe_load(f)
    send_email("client@example.com", "Test Campaign", "This is a test email.", config)