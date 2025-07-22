import streamlit as st
import pandas as pd
import datetime
from utils.fyers_api import get_authorization_url

st.set_page_config(page_title="Intraday Stock Screener", layout="wide")

st.title("🔍 Intraday Stock Screener (Live with Fyers API)")

# Placeholder stock data
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
st.dataframe(df, use_container_width=True)

# Filter by signal
signal = st.selectbox("Filter by Signal", options=["All", "Buy", "Sell", "Hold"])
if signal != "All":
    df = df[df["Buy/Sell Signal"] == signal]
    st.dataframe(df, use_container_width=True)

# Generate Fyers auth link (placeholder values)
client_id = "CC0LI2RTV4-100"
redirect_uri = "https://intraday-screener.streamlit.app"

st.markdown("---")
st.subheader("🔐 Fyers API Access Token")
auth_url = get_authorization_url(client_id, redirect_uri)
st.markdown(f"[Click here to authorize and get access token]({auth_url})", unsafe_allow_html=True)