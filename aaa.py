import requests
import json
from testDriver import testDriver
import UrlGenerators
import ShopInfo

def getProducts():
    #r = requests.get('https://www.packershoes.com/products.json?limit=250')
    #products = json.loads(r.text)['products']
    count = 250
    page = 1
    productList = []
    while count>=250:
        urlstr = 'https://www.packershoes.com/products.json?limit=250&page={}'.format(page)
        r = requests.get(urlstr)
        products = json.loads(r.text)['products']
        productList.extend(products)
        count = len(products)
        page += 1
    return productList

def getProductJson(product):
    urlstr = 'https://packershoes.com/products/{}.json'.format(product)
    r = requests.get(urlstr)
    jsonStr = json.loads(r.text)
    return jsonStr

#fix this
def findKeyword(product, keyword, type, price):
    keywordList = keyword.upper().split(' ')
    if any(word in product['title'] for word in keywordList):
        if price == '' or price in product['tags']:
            if 'email-orders' not in product['tags'] and 'phone-orders' not in product['tags'] \
                    and 'INQUIRE' not in product['tags']:
                if type.upper() in product['tags'] and type.upper() == "FOOTWEAR":
                    if (ProductAvailable(product, False)):
                        print(product['title'])
                        return product
                elif type.upper() in product['tags'] and type.upper() == "APPAREL":
                    if (ProductAvailable(product, False)):
                        print(product['title'])
                        return product
                elif type.upper() in product['tags'] and type.upper() == "ACCESSORIES":
                    if (ProductAvailable(product, False)):
                        print(product['title'])
                        return product
                # BOTH
                elif type.upper() == "ALL":
                    if (ProductAvailable(product, False)):
                        print(product['title'])
                        return product
    return None


def ReturnProduct(products, keyword):
    for p in products:
        if keyword.upper() == p['title']:
            return p
    return None

def getSizes(product):
    sizes = []
    for variant in product['variants']:
        if(variant['available']):
            sizes.append(variant['option1'])
    return sizes


def ProductAvailable(product, printSize):
    for variant in product['variants']:
        if(variant['available']):
            if(printSize):
                print("Size: ", variant['option1'])
            else:
                return True
    if(not printSize):
        return False


def CheckSizeMatch(product, size):
    for variant in product['variants']:
        if(variant['available']):
            if(size == variant['option1']):
                return True
    return False

#add quantity
def CompleteShopping():
    ProductList = ShopInfo.ShoppingKeys["Cart"]
    SizeList = ShopInfo.ShoppingKeys["Sizes"]
    QuantityList = ShopInfo.ShoppingKeys["Quantities"]
    initialPopUp = True
    UrlList = []
    for i in range(len(ProductList)):
        if (initialPopUp):
            PopUp = UrlGenerators.popUpGen(ProductList[i])
            initialPopUp = False
        URL = UrlGenerators.UrlGen(ProductList[i], SizeList[i])
        print(URL)
        UrlList.append(URL)
    checkouttest = testDriver(UrlList, PopUp, ProductList, QuantityList)
    checkouttest.checkout()

