import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus, urlparse, parse_qs
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

def get_price_from_walmart(product_name):
    url = 'https://www.walmart.com/search?q=' + quote_plus(product_name)
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        item_stack = soup.select('div[data-testid="item-stack"]')

        if item_stack:
            products = item_stack[0].find_all('div', class_='mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1')

            if products:
                for product in products:
                    role_group_element = product.select_one('div[role="group"]')
                    if role_group_element:
                        sponsor = role_group_element.select_one('div[data-testid="list-view"] div div[class="mt5 mb0"] div')
                        if not sponsor:
                            product_url = role_group_element.find('a')
                            if product_url:
                                product_url = product_url.get('href')
                                parsed_url = urlparse(product_url)
                                query_params = parse_qs(parsed_url.query)
                                final_url = query_params['rd'][0] if 'rd' in query_params else 'https://www.walmart.com' + product_url

                                price_text = role_group_element.select_one('div[data-testid="list-view"] div[data-automation-id="product-price"] div').text.strip()
                                if price_text:
                                    numbers_and_dots = re.findall(r'[0-9.]+', price_text)
                                    price = ''.join(numbers_and_dots)
                                    price = price[:-2] + '.' + price[-2:]
                                    price = float(price)
                                    return final_url, price
                                else:
                                    return final_url, "Price not available"
            else:
                return "Product not found", "N/A"
        else:
            return "Product not found", "N/A"
    else:
        raise Exception("Invalid Walmart search page response")