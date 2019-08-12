import requests
import json
from testDriver import testDriver
import UrlGenerators
import ShopInfo
import GUI
import sys
from PyQt5 import QtWidgets, QtGui

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

def Main():
    print("Collecting Packer Shoes Product Database...")
    products = getProducts()
    print("Collection Successful")
    # ask for shoe keyword
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
        print()
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

    checkouttest = testDriver(UrlList, PopUp, FinalProductList)
    checkouttest.checkout()
    '''
    try:
        testURL(UrlList, PopUp, driver)
        checkout(driver)
    except:
        print("Error, cannot find button / took too long to load")
    '''


if __name__ == "__main__":
    '''
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI.App()
    sys.exit(app.exec_())
    '''
    Main()
