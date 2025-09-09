import streamlit as st
import pandas as pd
import plotly.express as px
from utils import (
    categorize_transactions,
    monthly_summary,
    category_breakdown,
    top_vendors,
    detect_anomalies,
    generate_roast_summary,
)
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="💸 Money Buddy", layout="wide")

st.title("💸 Money Buddy – Your Savage Finance Bestie")
st.markdown("Upload your transaction file and let me roast your spending 😈")

# File Upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Ensure correct format
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Categorize
    df = categorize_transactions(df)

    # Summary
    st.subheader("📊 Expense Breakdown by Category")
    breakdown = category_breakdown(df)
    fig = px.bar(breakdown, x="Category", y="Amount", text="Amount")
    st.plotly_chart(fig, use_container_width=True)

    # Top vendors
    st.subheader("🏆 Top Vendors")
    st.dataframe(top_vendors(df))

    # Anomalies
    st.subheader("⚠️ Anomalies Detected")
    anomalies = detect_anomalies(df)
    if not anomalies.empty:
        st.dataframe(anomalies)
    else:
        st.write("No major anomalies 🚀")

    # Roast
    st.subheader("🔥 Roast of the Day")
    st.write(generate_roast_summary(df))
else:
    st.info("Upload a `sample_transactions.csv` file to get started.")
