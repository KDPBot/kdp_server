import streamlit as st
import pandas as pd
import requests
import os
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="Portfolios Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- 1. Get the API base URL from environment variables ---
API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")

# --- 2. Functions to fetch data from the FastAPI backend ---
@st.cache_data(ttl=600)  # Cache data for 10 minutes
def fetch_portfolio_data():
    """Fetches all portfolio data from the FastAPI backend."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/portfolios")
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "success":
            return pd.DataFrame(data["data"])
        else:
            st.error(f"API Error: {data.get('message', 'Unknown error')}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: Could not connect to the API. Please ensure it's running. Details: {e}")
        return pd.DataFrame()

# --- 3. Functions to clean the data ---
def clean_portfolio_data(df):
    """Cleans the spend column and converts date columns."""
    if df.empty:
        return df
    
    if "spend" in df.columns:
        df["spend"] = df["spend"].astype(str).apply(lambda x: re.sub(r'[^0-9.-]', '', x))
        df["spend"] = pd.to_numeric(df["spend"], errors='coerce').fillna(0)
    
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    if 'updated_at' in df.columns:
        df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')
        
    return df

# --- 4. Main Streamlit application ---
def main():
    # --- Header ---
    st.title("📊 Portfolios Dashboard")

    # --- Fetch and process data ---
    raw_portfolio_data = fetch_portfolio_data()
    cleaned_portfolio_data = clean_portfolio_data(raw_portfolio_data.copy())

    # --- Sidebar for VPS selection ---
    st.sidebar.title("Filters")
    vps_list = cleaned_portfolio_data['vps_name'].unique()
    selected_vps = st.sidebar.selectbox("Select a VPS", vps_list)

    # --- Filter data based on selected VPS ---
    filtered_portfolio_data = cleaned_portfolio_data[cleaned_portfolio_data['vps_name'] == selected_vps]

    # --- Portfolios Section ---
    st.header(f"📊 Portfolios for {selected_vps}")
    if filtered_portfolio_data.empty:
        st.warning("No portfolio data found for the selected VPS.")
    else:
        # Display last update time
        if "updated_at" in filtered_portfolio_data.columns and not filtered_portfolio_data['updated_at'].isna().all():
            last_updated = filtered_portfolio_data["updated_at"].max()
            st.caption(f"Last Updated: {last_updated.strftime('%B %d, %Y at %I:%M %p %Z')}")

        st.divider()

        # --- 1. Key Performance Indicators (KPIs) ---
        total_spend = filtered_portfolio_data["spend"].sum()
        total_portfolios = filtered_portfolio_data["portfolio_name"].nunique()

        st.subheader("📈 Portfolio At a Glance")
        kpi_cols = st.columns(2)
        kpi_cols[0].metric(label="Total Spend", value=f"${total_spend:,.2f}")
        kpi_cols[1].metric(label="Unique Portfolios", value=f"{total_portfolios}")
        
        st.divider()

        # --- 2. Detailed portfolio Performance ---
        st.subheader("📖 Detailed Portfolio Performance")
        
        with st.expander("View All Portfolios in Detail"):
            sort_col, order_col = st.columns(2)
            sort_by = sort_col.selectbox(
                "Sort portfolios by",
                options=["spend", "portfolio_name", "updated_at"],
                index=0,
                key="sort_portfolios"
            )
            ascending = order_col.checkbox("Ascending", key="asc_portfolios")
            
            sorted_df = filtered_portfolio_data.sort_values(by=sort_by, ascending=ascending)
            
            st.dataframe(
                sorted_df[["portfolio_name", "spend", "updated_at"]].style.format({
                    "spend": "${:,.2f}",
                    "updated_at": '{:%d/%m/%Y %I:%M %p}'
                }),
                use_container_width=True
            )
        
        st.divider()

if __name__ == "__main__":
    main()
