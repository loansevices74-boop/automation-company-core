import streamlit as st

from agents.ai_agent import AIAgent

st.set_page_config(page_title="Automation Company", layout="wide")

st.title("🚀 Automation Company Dashboard")
st.write("Welcome Mayor! Explore your automation pillars.")

if st.button("Run AI Agent", type="primary"):
    with st.spinner("Running automation agent..."):
        logs = AIAgent().run()

    st.success("Agent executed successfully!")
    st.subheader("Agent Logs")
    st.code("\n".join(logs), language="text")
