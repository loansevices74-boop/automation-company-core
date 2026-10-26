import streamlit as st
import pandas as pd
from agents.ai_agent import AIAgent

st.set_page_config(page_title="Automation Company", layout="wide")

st.title("🚀 Automation Company Dashboard")
st.write("Welcome Mayor! Explore your 27 automation pillars.")

if st.button("Run AI Agent"):
    agent = AIAgent()
    logs = agent.run()
    st.success("Agent executed successfully!")
    st.subheader("Agent Logs")
    st.write(logs)