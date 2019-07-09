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
        page += 1
    #print(len(productList))
    #print(productList[0])
    return productList


def findKeyword(products, keyword, type):
    pList = []
    for product in products:
        if type.upper() in product['product_type']:
            if keyword.upper() in product['title']:
                if(ProductAvailable(product, False)):
                    pList.append(product)
                    print(product['title'])
        elif keyword.upper() in product['title']:
            if(ProductAvailable(product, False)):
                pList.append(product)
                print(product['title'])
    if(len(pList)==0):
        return None
    return pList


def ReturnProduct(products, keyword):
    for p in products:
        if keyword.upper() == p['title']:
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


def CheckSizeMatch(product, size):
    for variant in product['variants']:
        if(variant['available']):
            if(size == variant['option1']):
                return True
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
    title = title.replace(" - ", "-")
    title = title.replace("  ", "-")
    title = title.replace(" ", "-")
    title = title.replace(",", "-")
    title = title.replace("/", "-")
    title = title.replace(". ", "")
    title = title.replace(".", "-")
    title = title.replace('-"', "-quot-")
    title = title.replace('"', "-quot")
    title = title.replace("'", "-39-")

    popUp = '// *[ @ id = "' + title + '"] / div[7] / div / div / div / button / img'

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


def testURL(urlList, PopUp, driver, productList):
    #Some urls have contact to order
    adClicked = False
    for num in range(len(urlList)):
        driver.get(urlList[num])
        if (not adClicked):
            time.sleep(3)
            driver.find_element_by_xpath(PopUp).click()
            adClicked = True

        for item in productList[num]['tags']:
            if(item == 'email-orders' or item == 'phone-orders'):
                print("This is a contact to order")
                return False
        driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
    return True


def checkout(driver):
    # STORE THESE IN A SEPARATE FILE (MODULARIZE). ADD OTHER OPTIONS TOO
    time.sleep(1)
    driver.find_element_by_xpath('// *[ @ id = "CartContainer"] / form / div[2] / button').click()
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')
    driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys('Lim')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('12345 Burger Dr.')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Cerritos')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('90703')
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('12345678910')

    time.sleep(10)

def Main():
    print("Collecting Packer Shoes Product Database...")
    products = getProducts()
    print("Collection Successful")
    #ask for shoe keyword
    DoneShopping = False
    UrlList = []
    FinalProductList = []
    PopUp = ""
    initialPopUp = True
    while(not DoneShopping):
        ProdList = None
        FinalProduct = None
        type = input("Enter Profuct Type: Footwear or Apparel or Both? ")

        keyword = input("Enter a keyword: ")
        while(ProdList==None):
            ProdList = findKeyword(products, keyword, type)
            if(ProdList == None):
                keyword = input("Keyword not found, please reenter: ")
            else:
                break
        ProductName = input("Enter Product Name from List: ")
        while(FinalProduct == None):
            FinalProduct = ReturnProduct(ProdList, ProductName)
            if(FinalProduct == None):
                ProductName = input("Invalid Product Name, Please Enter the Full Product Name: ")
            else:
                break
        print(FinalProduct)
        ProductAvailable(FinalProduct, True)
        print("Type Back to go back to Keyword Search")
        SizeIn = input("Enter an Available Size: ")
        SizeIn = SizeIn.upper()
        if(SizeIn == "BACK"):
            continue
        while(not CheckSizeMatch(FinalProduct, SizeIn)):
            SizeIn = input("Invalid Size, Please Enter an Available Size: ")
        if(initialPopUp):
            PopUp = popUpGen(FinalProduct)
            initialPopUp = False
        URL = UrlGen(FinalProduct, SizeIn)
        print(URL)
        UrlList.append(URL)
        FinalProductList.append(FinalProduct)
        isDone = input("Are You Done Shopping? Enter Yes or No ")
        if(isDone.lower() == "yes"):
            DoneShopping = True
    driver = webdriver.Chrome('./chromedriver')
    CanCheckOut = testURL(UrlList, PopUp, driver, FinalProductList)
    if(CanCheckOut):
        checkout(driver)
    else:
        print("Cannot check out")
    '''
    try:
        testURL(UrlList, PopUp, driver)
        checkout(driver)
    except:
        print("Error, cannot find button / took too long to load")
    '''
    driver.close()

Main()
'''
for product in products:
    print(product)
print(len(products))
'''