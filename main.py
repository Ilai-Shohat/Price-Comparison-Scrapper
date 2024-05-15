from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from scrapers.bestbuy import get_price_from_bestbuy
from scrapers.walmart import get_price_from_walmart
from scrapers.newegg import get_price_from_newegg
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specifies the origin domains (your frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api/prices")
def get_prices(product_name: str):
    try:
        bestbuy_title, bestbuy_price, bestbuy_url  = get_price_from_bestbuy(product_name)
        walmart_title, walmart_price, walmart_url= get_price_from_walmart(product_name)
        newegg_title, newegg_price, newegg_url = get_price_from_newegg(product_name)
        
        # Create a list of dictionaries, each representing one store's pricing info for the product
        prices = [
            {"store": "BestBuy", "price": bestbuy_price, "product": bestbuy_title, "url": bestbuy_url},
            {"store": "Walmart", "price": walmart_price, "product": walmart_title, "url": walmart_url},
            {"store": "Newegg", "price": newegg_price, "product": newegg_title, "url": newegg_url}
        ]

        # Structure the JSON response to be a dictionary with product names as keys and values as lists of store prices
        response = {"prices": prices}

        # prices = {
        #     "bestbuy": {
        #         "title": bestbuy_title,
        #         "price": bestbuy_price,
        #         "url": bestbuy_url
        #     },
        #     "walmart": {
        #         "title": walmart_title,
        #         "price": walmart_price,
        #         "url": walmart_url
        #     },
        #     "newegg": {
        #         "title": newegg_title,
        #         "price": newegg_price,
        #         "url": newegg_url
        #     }
        # }

        return JSONResponse(content=response)  

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)