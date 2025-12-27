import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from datetime import datetime
from io import StringIO
import yfinance as yf

SECTOR_MAP = {
    "AI & Software": ["RVLV", "SOUN", "ORCL"],
    "Semiconductors": ["INTC","TSM","000660.KS"],
    "Biotech": ["PFE","VSTM","068270.KS"],
    "Automotive": ["TSLA","LCID","TM"],
    "Drones": ["ACHR","033320.KQ","JOBY"],
    "Defense": ["079550.KS","000880.KS","012450.KS"],
}

COMPANY_INFO = {
    "RVLV": "ResolveAI — AI software company",
    "SOUN": "SoundHound AI — Voice AI leader",
    "ORCL": "Oracle — Global DB & cloud corporation",
    "INTC": "Intel — Semiconductor leader",
    "TSM": "TSMC — Largest chip foundry",
    "000660.KS": "SK Hynix — Memory semiconductor giant",
    "PFE": "Pfizer — Global pharmaceutical company",
    "VSTM": "Verastem — Cancer treatment R&D",
    "068270.KS": "Celltrion — Leading biosimilar company",
    "TSLA": "Tesla — EV market leader",
    "LCID": "Lucid — Premium EV manufacturer",
    "TM": "Toyota — Global automotive leader",
    "ACHR": "Archer Aviation — UAM pioneer",
    "033320.KQ": "JCH Systems — Drone & electronics company",
    "JOBY": "Joby — Air taxi developer",
    "079550.KS": "LIG Nex1 — Korean defense tech",
    "000880.KS": "Hanwha — Major defense manufacturer",
    "012450.KS": "Hanwha Aerospace — Aviation/defense core"
}

def fetch_stock(symbol):
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1y")
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        return None

st.set_page_config(page_title="Rising Stock Recommender", page_icon="📈", layout="centered")

page_style = """
<style>
    .stApp { background-color: #FFF0F0; }
    .main .block-container { text-align: center; }
    h1 { font-size: 3rem !important; font-weight: bold !important; color: #3c3c3c !important; }
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: bold !important;
    }
    [data-testid="stMetricValue"] {
        color: #000000 !important;
    }
    .stMarkdown p {
        font-size: 1.4rem;
        color: #000000 !important;
    }
    div.stButton { display: flex; justify-content: center; margin-top: 20px; }
    div.stButton > button { background-color: #3c3c3c; color: white; border-radius: 10px; padding: 10px 25px; font-size: 1.1rem; border: none; }
    .stock-info {
        color: #000000 !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        margin-top: 30px !important;
        text-align: center !important;
    }
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "start"

if st.session_state.page == "start":
    st.title("📈 Rising Stock Recommender")
    st.markdown("Discover the most promising stocks by sector 👇")
    if st.button("START ➜"):
        st.session_state.page = "select_sector"

sectors = list(SECTOR_MAP.keys())

if st.session_state.page == "select_sector":
    st.title("Choose a Sector")
    st.markdown("Which sector would you like to explore?")
    for sector in sectors:
        if st.button(sector):
            st.session_state.selected_sector = sector
            st.session_state.page = "result"

elif st.session_state.page == "result":
    sector = st.session_state.selected_sector
    st.title(f"📊 Recommended Stocks: {sector}")
    symbols = SECTOR_MAP.get(sector, [])

    for sym in symbols:
        st.markdown(f'<div class="stock-info">{sym} — {COMPANY_INFO.get(sym,"")}</div>', unsafe_allow_html=True)
        df = fetch_stock(sym)
        if df is not None and len(df) >= 2:
            last_price = df['Close'].iloc[-1]
            prev_price = df['Close'].iloc[-2]
            change = last_price - prev_price
            pct_change = (change / prev_price) * 100
            currency = "KRW" if sym.endswith(".KS") or sym.endswith(".KQ") else "USD"

            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric(label="Current Price", value=f"{last_price:,.2f} {currency}")
            with m_col2:
                st.metric(label="Daily Change", value=f"{change:,.2f} {currency}", delta=f"{pct_change:.2f}%")

            fig, ax = plt.subplots(figsize=(8, 3.5))
            ax.plot(df['Date'], df['Close'], color='#1f77b4', linewidth=2)
            ax.set_ylabel(f"Price ({currency})")
            ax.grid(True, linestyle='--', alpha=0.5)
            st.pyplot(fig)
        else:
            st.warning(f"Unable to load data for {sym}.")
        st.markdown("---")

    if st.button("🔙 Select Another Sector"):
        st.session_state.page = "select_sector"
        st.rerun()
