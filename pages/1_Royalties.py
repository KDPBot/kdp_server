import streamlit as st
import pandas as pd
import requests
import os
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="Royalties Dashboard",
    page_icon="👑",
    layout="wide"
)

# --- 1. Get the API base URL from environment variables ---
API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")

# --- 2. Functions to fetch data from the FastAPI backend ---
@st.cache_data(ttl=600)  # Cache data for 10 minutes
def fetch_royalty_data():
    """Fetches all royalty data from the FastAPI backend."""
    try:
        response = requests.get(f"{API_BASE_URL}/api/royalties")
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
def clean_royalty_data(df):
    """Cleans the total_royalties column and converts date columns."""
    if df.empty:
        return df
    
    if "total_royalties" in df.columns:
        df["total_royalties"] = df["total_royalties"].astype(str).apply(lambda x: re.sub(r'[^0-9.-]', '', x))
        df["total_royalties"] = pd.to_numeric(df["total_royalties"], errors='coerce').fillna(0)
    
    if 'updated_at' in df.columns:
        df['updated_at'] = pd.to_datetime(df['updated_at'], errors='coerce')
        
    return df

# --- 4. Main Streamlit application ---
def main():
    # --- Header ---
    st.title("👑 Royalties Dashboard")

    # --- Fetch and process data ---
    raw_royalty_data = fetch_royalty_data()
    cleaned_royalty_data = clean_royalty_data(raw_royalty_data.copy())

    # --- Sidebar for VPS selection ---
    st.sidebar.title("Filters")
    vps_list = cleaned_royalty_data['vps_name'].unique()
    selected_vps = st.sidebar.selectbox("Select a VPS", vps_list)

    # --- Filter data based on selected VPS ---
    filtered_royalty_data = cleaned_royalty_data[cleaned_royalty_data['vps_name'] == selected_vps]

    # --- Royalties Section ---
    st.header(f"👑 Royalties for {selected_vps}")
    if filtered_royalty_data.empty:
        st.warning("No royalty data found for the selected VPS.")
    else:
        # Display last update time
        if "updated_at" in filtered_royalty_data.columns and not filtered_royalty_data['updated_at'].isna().all():
            last_updated = filtered_royalty_data["updated_at"].max()
            st.caption(f"Last Updated: {last_updated.strftime('%B %d, %Y at %I:%M %p %Z')}")

        st.divider()

        # --- 1. Key Performance Indicators (KPIs) ---
        total_royalty = filtered_royalty_data["total_royalties"].sum()
        total_books = filtered_royalty_data["book_title"].nunique()

        st.subheader("📈 At a Glance")
        kpi_cols = st.columns(2)
        kpi_cols[0].metric(label="Total Royalties", value=f"${total_royalty:,.2f}")
        kpi_cols[1].metric(label="Unique Books", value=f"{total_books}")
        
        st.divider()

        # --- 2. Detailed Book Performance ---
        st.subheader("📖 Detailed Book Performance")
        
        with st.expander("View All Books in Detail"):
            sort_col, order_col = st.columns(2)
            sort_by = sort_col.selectbox(
                "Sort books by",
                options=["total_royalties", "book_title", "updated_at"],
                index=0,
                key="sort_books"
            )
            ascending = order_col.checkbox("Ascending", key="asc_books")
            
            sorted_df = filtered_royalty_data.sort_values(by=sort_by, ascending=ascending)
            
            st.dataframe(
                sorted_df[["book_title", "total_royalties", "updated_at"]].style.format({
                    "total_royalties": "${:,.2f}",
                    "updated_at": '{:%d/%m/%Y %I:%M %p}'
                }),
                use_container_width=True
            )
        
        st.divider()

if __name__ == "__main__":
    main()
