import requests
from bs4 import BeautifulSoup
import random
import time

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
]

def get_price_from_walmart(product_name):
    product_name = product_name.replace(" ", "+")
    url = f"https://www.walmart.com/search?q={product_name}"
    
    # Select a random user agent
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    
    # Add a random delay between requests
    time.sleep(random.uniform(1, 3))
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        items = soup.select("div[data-item-id]")
        
        if not items:
            return "Product not found", "N/A"
        
        for item in items:
            item_name_element = item.select_one("span.lh-title")
            if item_name_element:
                item_name = item_name_element.text.strip()
                price_element = item.select_one("div.lh-copy > span.lh-copy")
                if price_element:
                    price_text = price_element.text.strip().replace("$", "")
                    try:
                        price = float(price_text)
                        return item_name, price
                    except ValueError:
                        # Handle the case when the price is not a valid float
                        return item_name, "Price not available"
        
        return "Price not found", "N/A"
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        return "Error occurred while retrieving data from Walmart", str(e)
