import requests
import json

def getProducts():
    #r = requests.get('https://www.packershoes.com/products.json?limit=250')
    #products = json.loads(r.text)['products']
    count = 250
    page = 1
    productList = []
    while count>=250:
        #print(page)
        urlstr = 'https://www.packershoes.com/products.json?limit=250&page={}'.format(page)
        r = requests.get(urlstr)
        products = json.loads(r.text)['products']
        productList.extend(products)
        #print(len(products))
        count = len(products)
        page+=1
    #print(len(productList))
    #print(productList[0])
    return productList

def findKeyword(products, keyword):
    pList = []
    for product in products:
        if keyword.upper() in product['title']:
            pList.append(product)
            print(product['title'])
    finalProduct = input("Enter Product Name from List: ")
    for p in pList:
        if finalProduct == p['title']:
            return p
    return None

def ListSizes(product):
    count = 0
    for variant in product['variants']:
        #print(variant)
        if(variant['available']):
            print("Size: ", variant['option1'])
            count+=1
    if(count == 0):
        print("SOLD OUT")


def UrlGen(product, size):
    baseUrl = 'https://packershoes.com/collections/'

def Main():
    products = getProducts()
    #ask for shoe keyword
    keyword = input("Enter a keyword:" )
    FinalProduct = findKeyword(products, keyword)
    print(FinalProduct)
    ListSizes(FinalProduct)
    #SizeIn = int(input("Enter an Available Size: "))
    #UrlGen(FinalProduct,SizeIn)

Main()
'''
for product in products:
    print(product)
print(len(products))
'''