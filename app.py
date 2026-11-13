import streamlit as st

from core.qualification import qualify_lead
from core.store import Lead, LeadStore

st.set_page_config(page_title="B2B Automation Company", layout="wide")
st.title("B2B Automation Company")
st.caption("Administrator console: review, approve, and measure automation")

store = LeadStore()
leads = store.list()

cols = st.columns(4)
cols[0].metric("Leads", len(leads))
cols[1].metric("Qualified", sum(row["status"] == "qualified" for row in leads))
cols[2].metric("Customers", sum(row["status"] == "won" for row in leads))
cols[3].metric("Target MRR", "$5,000")

with st.sidebar:
    st.header("Add a lead")
    with st.form("lead_form", clear_on_submit=True):
        name = st.text_input("Contact name")
        email = st.text_input("Email")
        company = st.text_input("Company")
        source = st.selectbox("Source", ["manual", "website", "referral", "social"])
        submitted = st.form_submit_button("Save lead")
    if submitted:
        try:
            store.add(Lead(name=name, email=email, company=company, source=source))
            st.success("Lead saved for review.")
            st.rerun()
        except ValueError as error:
            st.error(str(error))

st.subheader("Qualification workspace")
with st.form("qualification_form"):
    company_for_score = st.text_input("Prospect company")
    need = st.text_area("Automation need")
    budget = st.number_input("Monthly budget (optional)", min_value=0, step=100, value=0)
    score_submitted = st.form_submit_button("Qualify without contacting")

if score_submitted:
    try:
        result = qualify_lead(company=company_for_score, need=need, budget=budget or None)
        st.metric("Qualification score", f"{result.score}/100")
        st.info(result.rationale)
        st.warning(result.next_action)
    except ValueError as error:
        st.error(str(error))

st.subheader("Lead pipeline")
if leads:
    st.dataframe(leads, use_container_width=True, hide_index=True)
else:
    st.info("No leads yet. Add the first prospect from the sidebar.")
