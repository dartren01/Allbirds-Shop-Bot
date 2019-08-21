import requests
import json
from testDriver import testDriver
import UrlGenerators
import ShopInfo

def getProducts():
    count = 250
    page = 1
    productList = []
    while count>=250:
        urlstr = 'https://www.allbirds.com/products.json?limit=250&page={}'.format(page)
        r = requests.get(urlstr)
        products = json.loads(r.text)['products']
        productList.extend(products)
        count = len(products)
        page += 1

    return productList

def getProductJson(product):
    urlstr = 'https://www.allbirds.com/products/{}.json'.format(product)
    r = requests.get(urlstr)
    jsonStr = json.loads(r.text)
    return jsonStr

def findProducts(product, keyword1, keyword2):
    # creates search param ex [mens, runners]
    keyword1 = keyword1.lower()
    keyword2 = keyword2.lower()
    titleList = [keyword1, keyword2]
    isAvailable = False
    for variant in product['variants']:
        if(variant['available']):
            isAvailable = True
            break
    if not isAvailable:
        return None
    if keyword1 == 'accessories' and product['product_type'].lower() == keyword1:
        return product
    elif keyword1 == 'socks' and product['product_type'].lower() == keyword1:
        return product
    elif keyword1 == 'smallbirds' and keyword1 in product['handle'].lower():
        return product
    elif all(word in product['handle'].split('-') for word in titleList):
        return product
    # no keyword, return all products
    elif keyword1 == keyword2:
        return product
    return None

def getSizes(product):
    sizes = []
    for variant in product['variants']:
        if(variant['available']):
            sizes.append(variant['option1'])
    return sizes

#add quantity
def CompleteShopping():
    ProductList = ShopInfo.ShoppingKeys["Cart"]
    SizeList = ShopInfo.ShoppingKeys["Sizes"]
    QuantityList = ShopInfo.ShoppingKeys["Quantities"]
    UrlList = []
    for i in range(len(ProductList)):
        URL = UrlGenerators.UrlGen(ProductList[i], SizeList[i])
        UrlList.append(URL)
    checkouttest = testDriver(UrlList, ProductList, QuantityList)
    checkouttest.checkout()
    return checkouttest

