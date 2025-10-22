# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
from database import init_db, add_royalty_data, get_all_royalties, add_portfolio_data, get_all_portfolios

# --- 1. Define the structure of the incoming data ---
class KDPPayload(BaseModel):
    accountIdentifier: str
    htmlContent: str # We now expect a string of HTML

# --- 2. Initialize the FastAPI app and CORS ---
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 3. Create the new parsing endpoint ---
@app.post("/api/parse")
async def parse_kdp_html(payload: KDPPayload):
    """
    This endpoint receives raw KDP Royalties Estimator HTML, 
    parses it, and extracts the tabular data.
    """
    print(f"Received HTML from account: {payload.accountIdentifier}")
    print("Starting HTML parsing...")
    print(payload.htmlContent[:500])  # Print the first 500 characters for debugging

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(payload.htmlContent, 'lxml')

    try:
        # --- NEW PARSING LOGIC ---
        extracted_data = []
        
        # Select all the rows in the table, including the header/summary row
        # Each book entry and the main summary is contained within a 'div' with class 'item'
        table_rows = soup.select("div.ui.items.no-margin.unstackable > div.item")

        for row in table_rows:
            # Check if the row is a book entry by looking for a book cover image
            if not row.select_one("img"):
                print("Skipping summary row...")
                continue

            # Find the element containing the book title or summary title (e.g., "All 5 books")
            title_element = row.select_one(".truncate-overflow")
            title = title_element.get_text(strip=True) if title_element else "Title Not Found"

            # The royalty values are in a specific row structure. We select all value columns.
            value_elements = row.select(".sixteen.wide.computer.column .row > div")

            # Extract text from each value column if it exists, otherwise default to "N/A"
            # The structure is consistent: 6 columns, first is empty, rest are the values.
            if len(value_elements) >= 6:
                ebook_royalties = value_elements[1].get_text(strip=True)
                print_royalties = value_elements[2].get_text(strip=True)
                kenp_royalties = value_elements[3].get_text(strip=True)
                total_royalties = value_elements[4].get_text(strip=True)
                total_royalties_usd = value_elements[5].get_text(strip=True)
            else:
                # Set default values if the structure isn't found
                ebook_royalties, print_royalties, kenp_royalties, total_royalties, total_royalties_usd = ["N/A"] * 5

            # Append the structured data for this row to our results list
            extracted_data.append({
                "bookTitle": title,
                "eBookRoyalties": ebook_royalties,
                "printRoyalties": print_royalties,
                "kenpRoyalties": kenp_royalties,
                "totalRoyalties": total_royalties,
                "totalRoyaltiesUSD": total_royalties_usd,
            })

        print("Successfully extracted data:")
        print(extracted_data)

        # Save the extracted_data to the database
        await add_royalty_data(payload.accountIdentifier, extracted_data)

        return {"status": "success", "data": extracted_data}

    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return {"status": "error", "message": str(e)}

# --- 4. Create the endpoint to fetch all royalty data ---
@app.get("/api/royalties")
async def get_royalties():
    """
    This endpoint fetches all royalty data from the database.
    """
    try:
        data = await get_all_royalties()
        return {"status": "success", "data": data}
    except Exception as e:
        print(f"Error fetching royalties: {e}")
        return {"status": "error", "message": str(e)}
    


@app.post("/api/parse_portfolios")
async def parse_portfolio_html(payload: KDPPayload): # We can reuse the KDPPayload
    """
    This endpoint receives raw Advertising Portfolio HTML, 
    parses it, and extracts a list of portfolio names and their spend.
    """
    print(f"Received Portfolio HTML from account: {payload.accountIdentifier}")
    print("Starting Portfolio HTML parsing...")
    
    soup = BeautifulSoup(payload.htmlContent, 'lxml')
    
    try:
        extracted_data = []
        
        # Find all name elements
        name_elements = soup.select('a[data-e2e-id="entityNameRenderer"]')
        
        # Find all spend elements from the data rows (not summary)
        spend_elements = soup.select('div[data-e2e-id="tableCell_cell_spend"] div[data-e2e-id="currencyRenderer"]')

        if not name_elements:
            print("Warning: No portfolio names found with selector 'a[data-e2e-id=\"entityNameRenderer\"]'")
        if not spend_elements:
             print("Warning: No spend values found with selector 'div[data-e2e-id=\"tableCell_cell_spend\"] div[data-e2e-id=\"currencyRenderer\"]'")

        
        # Pair the names and spends. We assume they appear in the same order.
        for name_tag, spend_tag in zip(name_elements, spend_elements):
            name = name_tag.get_text(strip=True)
            # .get_text() will correctly handle the <br> inside the div
            spend = spend_tag.get_text(strip=True) 
            
            extracted_data.append({
                "portfolio_name": name,
                "spend": spend
            })
        
        print("Successfully extracted portfolio data:")
        print(extracted_data)
        
        # Save the extracted_data to the database
        await add_portfolio_data(payload.accountIdentifier, extracted_data)

        return {"status": "success", "data": extracted_data}
    
    except Exception as e:
        print(f"Error parsing Portfolio HTML: {e}")
        return {"status": "error", "message": str(e)}

# --- 5. Create the endpoint to fetch all portfolio data ---
@app.get("/api/portfolios")
async def get_portfolios():
    """
    This endpoint fetches all portfolio data from the database.
    """
    try:
        data = await get_all_portfolios()
        return {"status": "success", "data": data}
    except Exception as e:
        print(f"Error fetching portfolios: {e}")
        return {"status": "error", "message": str(e)}
