import re
import requests
from bs4 import BeautifulSoup

def get_html(url):
    connection = requests.get(url, headers={"content-type" : "text/html; charset=utf-8", "content-encoding": "gzip", 'User-Agent': 'Chrome'})
    print(connection.status_code)

    if connection.status_code == 200:
        connection.cookies.clear()
        connection.close()
        return connection.content   
    else:
        connection.cookies.clear()
        connection.close()
        return None
    
    

def get_data_from_url(url):
    html_content = get_html(url)

    if html_content is None:
        return None
    
    soup = BeautifulSoup(html_content, 'html.parser')
    products = soup.find_all('div', class_='a-section a-spacing-small s-padding-left-small s-padding-right-small')
    products_price = soup.find_all('span', class_='a-offscreen')


    products_response = []
    for product in products:
        try:
            product_name = product.find('span', class_='a-size-base-plus a-color-base a-text-normal').text
            products_price = product.find('span', class_='a-offscreen').text
            products_response.append({"name": product_name, "price": products_price})
        except:
            continue

    return products_response


def clean_data(data:list):
    cleaned_data = []
    for product in data:
        product_name = product['name']
        product_price = product['price']
        product_name = re.sub(r'[^a-zA-Z0-9 ]', ' ', product_name)
        product_price = re.sub(r'[^a-zA-Z0-9 ]', ' ', product_price)
        cleaned_data.append({"name": product_name, "price": product_price})
    return cleaned_data

