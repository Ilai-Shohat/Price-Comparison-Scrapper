import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def get_price_from_bestbuy(product_name):
    str_item = quote_plus(product_name)
    url = f'https://www.bestbuy.com/site/searchpage.jsp?st={str_item}&intl=nosplash'
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        items = soup.find_all('li', class_='sku-item')
        
        if items:
            item = items[0]
            title = item.find('h4', class_='sku-title').text.strip()
            item_page_link = item.find('h4', class_='sku-title').a['href']
            
            if item_page_link:
                full_item_page_link = f'https://www.bestbuy.com{item_page_link}&intl=nosplash'
                item_page_response = requests.get(full_item_page_link, headers=HEADERS)
                
                if item_page_response.status_code == 200:
                    item_page_soup = BeautifulSoup(item_page_response.content, "html.parser")
                    price_element = item_page_soup.find('div', class_='priceView-hero-price priceView-customer-price')
                    if price_element:
                        price = price_element.span.text.strip()
                        price = float(price.replace('$', '').replace(',', ''))
                        return title, price, full_item_page_link
                    else:
                        return title, "Price not available", full_item_page_link
                else:
                    return title, "Price not available", full_item_page_link
            else:
                return title, "Price not available", full_item_page_link
        else:
            return "Product not found", "N/A", 
    else:
        return "Error in request", "N/A"
