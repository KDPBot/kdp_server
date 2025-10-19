import os
import asyncpg
from urllib.parse import urlparse

# --- 1. Get the database connection details from environment variables ---


# Get the database connection details from environment variables
DATABASE_URL = "postgresql://postgres:quHgWyGZsgCTcehtsmsaZxsvMMayECdV@caboose.proxy.rlwy.net:15764/railway"

# --- 2. Define the database initialization function ---
async def init_db():
    """
    Initializes the database and creates the 'royalties' table if it doesn't exist.
    This function now connects to a PostgreSQL database.
    """
    if not DATABASE_URL:
        raise Exception("DATABASE_URL environment variable not set.")

    conn = await asyncpg.connect(DATABASE_URL)
    try:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS royalties (
                id SERIAL PRIMARY KEY,
                vps_name VARCHAR(255) NOT NULL,
                book_title VARCHAR(255) NOT NULL,
                total_royalties VARCHAR(255) NOT NULL
            )
        """)
        print("Database initialized successfully.")
    finally:
        await conn.close()

# --- 3. Define the function to add royalty data ---
async def add_royalty_data(vps_name: str, data: list):
    """
    Adds new royalty data for a given VPS to the PostgreSQL database.
    It first deletes all existing data for that VPS and then inserts the new data.
    """
    if not DATABASE_URL:
        raise Exception("DATABASE_URL environment variable not set.")

    conn = await asyncpg.connect(DATABASE_URL)
    try:
        async with conn.transaction():
            # Delete existing data for the given vps_name
            await conn.execute("DELETE FROM royalties WHERE vps_name = $1", vps_name)

            # Prepare data for insertion
            insert_data = [(vps_name, item['bookTitle'], item['totalRoyaltiesUSD']) for item in data]

            # Insert the new data using copy_records_to_table for efficiency
            await conn.copy_records_to_table(
                'royalties',
                records=insert_data,
                columns=['vps_name', 'book_title', 'total_royalties']
            )

        print(f"Successfully added {len(data)} records for VPS: {vps_name}")
    finally:
        await conn.close()

# --- 4. Define a function to fetch all royalty data ---
async def get_all_royalties():
    """
    Fetches all royalty data from the database.
    """
    if not DATABASE_URL:
        raise Exception("DATABASE_URL environment variable not set.")

    conn = await asyncpg.connect(DATABASE_URL)
    try:
        records = await conn.fetch("SELECT vps_name, book_title, total_royalties FROM royalties")
        return [dict(record) for record in records]
    finally:
        await conn.close()
