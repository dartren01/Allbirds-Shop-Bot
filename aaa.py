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
            if(ProductAvailable(product, False)):
                pList.append(product)
                print(product['title'])
    finalProduct = input("Enter Product Name from List: ")
    #add exception checks
    for p in pList:
        if finalProduct.upper() == p['title']:
            return p
    return None


def ProductAvailable(product, printSize):
    for variant in product['variants']:
        if(variant['available']):
            if(printSize):
                print("Size: ", variant['option1'])
            else:
                return True
    if(not printSize):
        return False


'''
def ListSizes(product):
    count = 0
    for variant in product['variants']:
        #print(variant)
        if(variant['available']):
            print("Size: ", variant['option1'])
            count+=1
'''

def popUpGen(product):
    title = str(product['title'])
    title = title.lower()
    title = title.replace("  ", "-")
    title = title.replace(" ", "-")
    title = title.replace('-"', "-quot-")
    title = title.replace('"', "-quot")

    popUp = '// *[ @ id = "' + title + '"] / div[7] / div / div / div / button'
    return popUp

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

def testURL(url, popUp):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
    time.sleep(2)
    driver.find_element_by_xpath(popUp).click()

    driver.find_element_by_xpath('//*[@id="CartContainer"]/form/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')
    time.sleep(10)
    driver.close()
    #driver.find_element_by_xpath("//html").click();


def Main():
    products = getProducts()
    #ask for shoe keyword
    keyword = input("Enter a keyword: ")
    FinalProduct = findKeyword(products, keyword)
    print(FinalProduct)
    ProductAvailable(FinalProduct, True)
    SizeIn = input("Enter an Available Size: ")
    PopUp = popUpGen(FinalProduct)
    URL = UrlGen(FinalProduct, SizeIn)
    print(URL)
    testURL(URL, PopUp)

Main()
'''
for product in products:
    print(product)
print(len(products))
'''