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
        urlstr = 'https://www.allbirds.com/products.json?limit=250&page={}'.format(page)
        r = requests.get(urlstr)
        products = json.loads(r.text)['products']
        productList.extend(products)
        count = len(products)
        page += 1
    print("here")
    for x in range(len(productList)):
        print(productList[x])
    print("here")

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
    if keyword1 == 'accessories' and product['product_type'].lower() == keyword1:
        print(product['title'])
        return product
    elif keyword1 == 'socks' and product['product_type'].lower() == keyword1:
        print(product['title'])
        return product
    elif keyword1 == 'smallbirds' and keyword1 in product['handle'].lower():
        print(product['title'])
        return product
    elif all(word in product['handle'].split('-') for word in titleList):
        print(product['title'])
        return product
    return None

'''
#fix this
def findKeyword(product, keyword, type, price):
    keywordList = keyword.upper().split(' ')
    if any(word in product['title'] for word in keywordList):
        if price == '' or price in product['tags']:
                if type.upper() in product['tags'] and type.upper() == "FOOTWEAR":
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
'''

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
    #initialPopUp = False
    UrlList = []
    for i in range(len(ProductList)):
        #if (initialPopUp):
            #PopUp = UrlGenerators.popUpGen(ProductList[i])
            #initialPopUp = False
        URL = UrlGenerators.UrlGen(ProductList[i], SizeList[i])
        print(URL)
        UrlList.append(URL)
    checkouttest = testDriver(UrlList, ProductList, QuantityList)
    checkouttest.checkout()

