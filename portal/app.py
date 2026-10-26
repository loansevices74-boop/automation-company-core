from flask import Flask, render_template, request, redirect
import pandas as pd
import yaml

app = Flask(__name__)

with open("portal/config.yml") as f:
    config = yaml.safe_load(f)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", company=config['company_name'])

@app.route("/reports")
def reports():
    try:
        df = pd.read_csv("reports/daily_report.csv")
        return render_template("reports.html", data=df.to_html())
    except FileNotFoundError:
        return "No reports available."

@app.route("/billing")
def billing():
    try:
        df = pd.read_csv("billing/payments.csv")
        return render_template("billing.html", data=df.to_html())
    except FileNotFoundError:
        return "No billing records available."

@app.route("/subscriptions")
def subscriptions():
    try:
        df = pd.read_csv("subscriptions/clients.csv")
        return render_template("subscriptions.html", data=df.to_html())
    except FileNotFoundError:
        return "No subscriptions yet."

if __name__ == "__main__":
    app.run(port=config['portal_port'])