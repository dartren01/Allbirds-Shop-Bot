import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ShopInfo

class testDriver:
    def __init__(self, UrlList, PopUp, FinalProductList, QuantityList):
        self.urls = UrlList
        self.Popup = PopUp
        self.FinalProdList = FinalProductList
        self.QuantityList = QuantityList

    def testURL(self, driver):
        # Some urls have contact to order
        adClicked = False
        for num in range(len(self.urls)):
            driver.get(self.urls[num])
            if (not adClicked):
                time.sleep(2)
                driver.find_element_by_xpath(self.Popup).click()
                adClicked = True

            for item in self.FinalProdList[num]['tags']:
                if (item == 'email-orders' or item == 'phone-orders'):
                    print("This is a contact to order")
                    return False
            for quantity in range(self.QuantityList[num]-1):
                driver.find_element_by_xpath('//*[@id="AddToCartForm--'
                                             'product-packer-template"]/div[2]/div/button[2]').click()
            driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
        return True

    def login_to_gmail(self, driver):
        email = ShopInfo.Login["Email"][0]
        password = ShopInfo.Login["Password"][0]

        driver.get('http://gmail.com')
        driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email + Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password + Keys.ENTER)
        return True

    def checkout(self):
        phone = ShopInfo.Login["Phone"][0]
        firstname = ShopInfo.Login["FirstName"][0]
        lastname = ShopInfo.Login["LastName"][0]
        address = ShopInfo.Login["Address"][0]
        city = ShopInfo.Login["City"][0]
        zipcode = ShopInfo.Login["Zipcode"][0]
        email = ShopInfo.Login["Email"][0]

        # ----- TEST CASES -----
        # phone = '5629165122'
        # firstname = 'carmine'
        # lastname = 'choi'
        # address = '19611 Jacob Ave'
        # city = 'cerritos'
        # zipcode = '90703'
        # email = 'gangmin519@gmail.com'


        driver = webdriver.Chrome('./chromedriver')

        if not self.login_to_gmail(driver):
            return False
        time.sleep(1)
        if not self.testURL(driver):
            print("Cannot Order")
            return False

        # ADD OTHER OPTIONS TOO
        time.sleep(1)
        driver.find_element_by_xpath('// *[ @ id = "CartContainer"] / form / div[2] / button').click()

        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(firstname)
        driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys(lastname)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(address)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(city)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(zipcode)
        driver.find_element_by_xpath('// *[ @ id = "checkout_email"]').send_keys(email)

        #driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        # time.sleep(30)
        # driver.close()