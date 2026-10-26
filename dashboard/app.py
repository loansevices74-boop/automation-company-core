import streamlit as st
import pandas as pd
import yaml

with open("dashboard/config.yml") as f:
    config = yaml.safe_load(f)

st.set_page_config(page_title=config['company_name'], layout="wide")

st.title(f"{config['company_name']} Admin Dashboard")

# CRM Section
st.header("Client Management")
try:
    crm_data = pd.read_csv("crm/client_data.csv")
    st.dataframe(crm_data)
except FileNotFoundError:
    st.write("No client data available yet.")

# Reports Section
st.header("Data Reports")
try:
    report = pd.read_csv("reports/daily_report.csv")
    st.dataframe(report.head(10))
except FileNotFoundError:
    st.write("No reports generated yet.")

# Billing Section
st.header("Billing & Payments")
try:
    payments = pd.read_csv("billing/payments.csv")
    st.dataframe(payments)
except FileNotFoundError:
    st.write("No payments logged yet.")