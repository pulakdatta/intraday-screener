
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Intraday Stock Screener", layout="wide")

st.title("🔍 Intraday Stock Screener (Demo)")
st.write("This is a placeholder dashboard to test deployment.")

# Sample placeholder data
data = {
    "Stock": ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK"],
    "Price": [2845, 3770, 1510, 1650, 1080],
    "RSI": [65, 40, 72, 55, 48],
    "VWAP": [2830, 3750, 1500, 1645, 1075],
    "Buy/Sell Signal": ["Buy", "Hold", "Sell", "Buy", "Hold"]
}

df = pd.DataFrame(data)

# Show last updated time
st.caption(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Display table
st.dataframe(df, use_container_width=True)

# Basic signal filter
signal = st.selectbox("Filter by Signal", options=["All", "Buy", "Sell", "Hold"])
if signal != "All":
    df = df[df["Buy/Sell Signal"] == signal]
    st.dataframe(df, use_container_width=True)

st.success("✅ You can now test this app on Streamlit Cloud.")
