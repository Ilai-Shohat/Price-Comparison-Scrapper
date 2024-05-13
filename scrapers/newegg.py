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

def get_price_from_newegg(product_name):
    product_name = product_name.replace(" ", "+")
    url = f"https://www.newegg.com/p/pl?d={product_name}"
    
    # Select a random user agent
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    
    # Add a random delay between requests
    time.sleep(random.uniform(1, 3))
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.find_all("div", class_="item-container")
        
        if not items:
            return "Product not found", "N/A"
        
        for item in items:
            item_action_div = item.find("div", class_="item-action")
            if item_action_div:
                price_div = item_action_div.find("ul", class_="price")
                if price_div:
                    price_current_li = price_div.find("li", class_="price-current")
                    if price_current_li:
                        strong = price_current_li.find("strong")
                        if strong:
                            item_title = item.find("a", class_="item-title").text.strip()
                            item_url = item.find("a", class_="item-img")["href"]
                            break
        
        if not item_url:
            return "Product not found", "N/A"
        
        response = requests.get(item_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            row_side_div = soup.find("div", class_="row-side")
            
            if not row_side_div:
                return item_title, "Price not found"
            
            price = row_side_div.find("li", class_="price-current")
            
            if not price:
                return item_title, "Price not found"
            
            dollar_price = price.find("strong").text
            cents_price = price.find("sup").text
            
            if not dollar_price or not cents_price:
                return item_title, "Price not found"
            
            price = dollar_price + cents_price
            price = price.replace(",", "")
            price = float(price)
            
            return item_title, price
        else:
            return "Invalid Newegg product page response", "N/A"
    else:
        return "Invalid Newegg search page response", "N/A"
