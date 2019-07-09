import requests
import json
from selenium import webdriver
from testDriver import testDriver
import UrlGenerators

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

def GetContactToOrder():
    contactToOrder = input("Include Contact to Order Items? Enter Yes or No: ")
    if (contactToOrder.lower() == 'yes'):
        return True
    return False

def findKeyword(products, keyword, type, contactToOrder):
    pList = []
    for product in products:
        if type.upper() in product['product_type']:
            if keyword.upper() in product['title']:
                if(ProductAvailable(product, False)):
                    pList.append(product)
                    print(product['title'])
        elif keyword.upper() in product['title']:
            if(ProductAvailable(product, False)):
                if(not contactToOrder):
                    if ('email-orders' not in product['tags'] and 'phone-orders' not in product['tags']):
                        pList.append(product)
                        print(product['title'])
                else:
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
        type = input("Enter Product Type: Footwear or Apparel or Both? ")
        keyword = input("Enter a keyword (EX. Nike): ")
        contact = GetContactToOrder()
        while(ProdList==None):
            ProdList = findKeyword(products, keyword, type, contact)
            if(ProdList == None):
                print()
                print("Keyword or products not found. Resetting Search.")
                print()
                type = input("Enter Product Type: Footwear or Apparel or Both? ")
                keyword = input("Enter a keyword (EX. Nike): ")
                contact = GetContactToOrder()
            else:
                break
        print()
        ProductName = input("Enter Product Name from List: ")
        while(FinalProduct == None):
            FinalProduct = ReturnProduct(ProdList, ProductName)
            if(FinalProduct == None):
                ProductName = input("Invalid Product Name, Please Enter the Full Product Name: ")
            else:
                break
        print()
        print(FinalProduct)
        ProductAvailable(FinalProduct, True)
        print("Type Back to go back to Keyword Search")

        SizeIn = input("Enter an Available Size: ")
        SizeIn = SizeIn.upper()
        if (SizeIn == "BACK"):
            continue
        while(not CheckSizeMatch(FinalProduct, SizeIn)):
            SizeIn = input("Invalid Size, Please Enter an Available Size: ")
            if (SizeIn == "BACK"):
                break

        if(initialPopUp):
            PopUp = UrlGenerators.popUpGen(FinalProduct)
            initialPopUp = False
        URL = UrlGenerators.UrlGen(FinalProduct, SizeIn)
        print(URL)
        UrlList.append(URL)
        FinalProductList.append(FinalProduct)
        print()
        isDone = input("Are You Done Shopping? Enter Yes or No ")
        if(isDone.lower() == "yes"):
            DoneShopping = True
    print()

    driver = webdriver.Chrome('./chromedriver')
    checkouttest = testDriver(UrlList, PopUp, FinalProductList, driver)
    checkouttest.checkout()
    '''
    try:
        testURL(UrlList, PopUp, driver)
        checkout(driver)
    except:
        print("Error, cannot find button / took too long to load")
    '''
    driver.close()


if __name__ == "__main__":
    Main()
