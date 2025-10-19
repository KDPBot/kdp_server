import streamlit as st
import pandas as pd
import requests
import os
import re

# --- 1. Get the API base URL from environment variables ---
API_BASE_URL = os.environ.get("DATABASE_URL", "http://localhost:8000")

# --- 2. Function to fetch data from the FastAPI backend ---
def fetch_data():
    """Fetches all data from the FastAPI backend."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/royalties")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data["status"] == "success":
            return pd.DataFrame(data["data"])
        else:
            st.error(f"Error fetching data from API: {data.get('message', 'Unknown error')}")
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to the API: {e}")
        return pd.DataFrame()

# --- 3. Function to clean the royalty data ---
def clean_royalty_data(df):
    """Cleans the total_royalties column by removing non-numeric characters and converting to float."""
    if "total_royalties" in df.columns:
        # Remove any characters that are not digits, a decimal point, or a minus sign
        df["total_royalties"] = df["total_royalties"].astype(str).apply(lambda x: re.sub(r'[^0-9.-]', '', x))
        # Convert to numeric, coercing errors to NaN (Not a Number)
        df["total_royalties"] = pd.to_numeric(df["total_royalties"], errors='coerce')
        # Fill any resulting NaN values with 0
        df.fillna(0, inplace=True)
    return df

# --- 4. Main Streamlit application ---
def main():
    st.set_page_config(layout="wide")
    st.title("KDP Royalties Dashboard")

    # Fetch and clean the data
    raw_data = fetch_data()
    
    if raw_data.empty:
        st.warning("No data found. Please ensure the FastAPI backend is running and has processed some data.")
        return

    cleaned_data = clean_royalty_data(raw_data)

    # --- Sidebar for Filtering ---
    st.sidebar.header("Filter Data")
    
    # Get unique VPS names for the filter
    vps_list = cleaned_data["vps_name"].unique()
    selected_vps = st.sidebar.multiselect("Select VPS", vps_list, default=vps_list)

    # Filter data based on selection
    if selected_vps:
        filtered_data = cleaned_data[cleaned_data["vps_name"].isin(selected_vps)]
    else:
        filtered_data = cleaned_data

    # --- Main Page Display ---
    st.header("Analytics Overview")

    if not filtered_data.empty:
        # --- Key Metrics ---
        total_royalty = filtered_data["total_royalties"].sum()
        total_books = filtered_data["book_title"].nunique()
        avg_royalty = filtered_data["total_royalties"].mean()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Royalties", f"${total_royalty:,.2f}")
        col2.metric("Total Books", total_books)
        col3.metric("Average Royalty per Book", f"${avg_royalty:,.2f}")

        # --- Data Visualization ---
        st.subheader("Royalties per Book")
        
        # Group by book title and sum royalties for the chart
        chart_data = filtered_data.groupby("book_title")["total_royalties"].sum().sort_values(ascending=False)
        st.bar_chart(chart_data)

        # --- Data Table ---
        st.subheader("Detailed Data")
        st.dataframe(filtered_data.style.format({"total_royalties": "${:,.2f}"}))
    else:
        st.info("No data available for the selected filters.")

if __name__ == "__main__":
    main()
