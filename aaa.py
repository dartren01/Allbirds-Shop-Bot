import requests
import json
from selenium import webdriver
import time

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
            if(ProductAvailable(product)):
                pList.append(product)
                print(product['title'])
    finalProduct = input("Enter Product Name from List: ")
    for p in pList:
        if finalProduct == p['title']:
            return p
    return None

def ProductAvailable(product):
    for var in product['variants']:
        if(var['available']):
            return True
    return False

def ListSizes(product):
    count = 0
    for variant in product['variants']:
        #print(variant)
        if(variant['available']):
            print("Size: ", variant['option1'])
            count+=1


def UrlGen(product, size):
    baseUrl = 'https://packershoes.com/collections/'
    brand = product['vendor'].lower()
    productName = product['handle']
    sizeVariant = product['id']
    for variant in product['variants']:
        if(size == variant['option1']):
            sizeVariant = variant['id']
    finalUrl = baseUrl + brand + '/products/' + productName + '?variant=' + str(sizeVariant)
    return finalUrl

def testURL(url):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
    time.sleep(2)
    driver.find_element_by_xpath("//html").click();
    #// *[ @ id = "new-balance-m990nv5-quot-made-in-the-usa-quot"] / div[7] / div / div / div / button
    #driver.find_element_by_xpath('//*[@id="adidas-consortium-magmur-runner-x-naked"]/div[7]/div').click()
    driver.find_element_by_xpath('//*[@id="CartContainer"]/form/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')

    #driver.find_element_by_xpath("//html").click();

def Main():
    products = getProducts()
    #ask for shoe keyword
    keyword = input("Enter a keyword: ")
    FinalProduct = findKeyword(products, keyword)
    print(FinalProduct)
    ListSizes(FinalProduct)
    SizeIn = input("Enter an Available Size: ")
    URL = UrlGen(FinalProduct, SizeIn)
    print(URL)
    #testURL(URL)

Main()
'''
for product in products:
    print(product)
print(len(products))
'''