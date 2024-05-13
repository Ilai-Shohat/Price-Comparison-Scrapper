from fastapi import FastAPI, HTTPException
from scrapers.bestbuy import get_price_from_bestbuy
from scrapers.walmart import get_price_from_walmart
from scrapers.newegg import get_price_from_newegg
import uvicorn

app = FastAPI()

@app.get("/prices")
def get_prices(product_name: str):
    try:
        bestbuy_title, bestbuy_price = get_price_from_bestbuy(product_name)
        walmart_title, walmart_price = get_price_from_walmart(product_name)
        newegg_title, newegg_price = get_price_from_newegg(product_name)

        prices = {
            "bestbuy": {
                "title": bestbuy_title,
                "price": bestbuy_price
            },
            "walmart": {
                "title": walmart_title,
                "price": walmart_price
            },
            "newegg": {
                "title": newegg_title,
                "price": newegg_price
            }
        }

        return prices

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)