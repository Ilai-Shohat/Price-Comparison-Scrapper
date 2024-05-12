from scrapers.bestbuy import get_price_from_bestbuy
from scrapers.walmart import get_price_from_walmart
from scrapers.newegg import get_price_from_newegg

def main():
    product_name = input("Enter the product name: ")
    
    try:
        bestbuy_title, bestbuy_price = get_price_from_bestbuy(product_name)
        # walmart_title, walmart_price = get_price_from_walmart(product_name)
        # newegg_title, newegg_price = get_price_from_newegg(product_name)
        
        print("Site\t\tItem Title Name\t\tPrice (USD)")
        print("-------------------------------------------------------")
        
        if bestbuy_title != "Product not found":
            print(f"Bestbuy.com\t{bestbuy_title}\t{bestbuy_price}")
        else:
            print(f"Bestbuy.com\tProduct not found")
        
        # if walmart_title != "Product not found":
        #     print(f"Walmart.com\t{walmart_title}\t{walmart_price}")
        # else:
        #     print(f"Walmart.com\tProduct not found")
        
        # if newegg_title != "Product not found":
        #     print(f"Newegg.com\t{newegg_title}\t{newegg_price}")
        # else:
        #     print(f"Newegg.com\tProduct not found")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()