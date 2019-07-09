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
    return p #for now return p, add check


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
    #some urls need to replace w's???
    '''
    EX:
    // *[ @ id = "adidas-x-stella-mccartney-w-39-s-ultraboost-x"] / div[7] / div / div / div / button / img
    // *[ @ id = "adidas-x-stella-mccartney-w's-ultraboost-x"] / div[7] / div / div / div / button / img
    '''
    popUp = '// *[ @ id = "' + title + '"] / div[7] / div / div / div / button / img'
    print(popUp)

    print(title)

    '''
    Testing Purposes
    // *[ @ id = "nike-air-max-1-quot-red-orbit-quot"] / div[7] / div / div / div / button / img
    //*[@id="adidas-ultraboost-s-by-stella-mccartney"]/div[7]/div/div/div/button/img
    
    ADIDAS Y-3 OVERSIZED BOMBER - BLACK
    //*[@id="adidas-y-3-oversized-bomber-black"]/div[7]/div/div/div/button/img
    //*[@id="adidas-y-3-oversized-bomber---black"]/div[7]/div/div/div/button/img
    
    ADIDAS CONSORTIUM ZX 10,000 C
    //*[@id="adidas-consortium-zx-10-000-c"]/div[7]/div/div/div/button/img
    //*[@id="adidas-consortium-zx-10,000-c"]/div[7]/div/div/div/button/img
    
    NIKE NSW JUST DO IT S/S T-SHIRT
    //*[@id="nike-nsw-just-do-it-s-s-t-shirt"]/div[7]/div/div/div/button/img
    //*[@id="nike-nsw-just-do-it-s/s-t-shirt"]/div[7]/div/div/div/button/img
    
    ADIDAS W'PUREBOOST X TR 3.0 BY STELLA MCCARTNEY
    //*[@id="adidas-w-39-pureboost-x-tr-3-0-by-stella-mccartney"]/div[7]/div/div/div/button/img
    //*[@id="adidas-w-39-pureboost-x-tr-30-by-stella-mccartney"]/div[7]/div/div/div/button/img
    
    NIKE AIR MAX 98 OA  "LA MEZCLA"

    '''

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


def testURL(urlList, PopUp, driver):
    #Some urls have contact to order
    adClicked = False
    for url in urlList:
        driver.get(url)
        if (not adClicked):
            time.sleep(3)
            driver.find_element_by_xpath(PopUp).click()
            adClicked = True
        driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()



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
    products = getProducts()
    #ask for shoe keyword
    DoneShopping = False
    UrlList = []
    PopUp = ""
    initialPopUp = True
    while(not DoneShopping):
        keyword = input("Enter a keyword: ")
        FinalProduct = findKeyword(products, keyword)
        print(FinalProduct)
        ProductAvailable(FinalProduct, True)
        print("Type Back to go back to Keyword Search")
        SizeIn = input("Enter an Available Size: ")
        if(SizeIn.lower() == "back"):
            continue
        if(initialPopUp):
            PopUp = popUpGen(FinalProduct)
            initialPopUp = False
        URL = UrlGen(FinalProduct, SizeIn)
        print(URL)
        UrlList.append(URL)
        isDone = input("Are You Done Shopping? Enter Yes or No ")
        if(isDone.lower() == "yes"):
            DoneShopping = True
    driver = webdriver.Chrome('./chromedriver')
    testURL(UrlList, PopUp, driver)
    checkout(driver)
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