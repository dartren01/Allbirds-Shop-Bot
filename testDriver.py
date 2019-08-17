import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ShopInfo
import GUI

class testDriver:
    def __init__(self, UrlList, FinalProductList, QuantityList):
        self.urls = UrlList
        #self.Popup = PopUp
        self.FinalProdList = FinalProductList
        self.QuantityList = QuantityList

    def testURL(self, driver):
        # Some urls have contact to order
        #adClicked = False
        for num in range(len(self.urls)):
            driver.get(self.urls[num])
            #if (not adClicked):
            #    time.sleep(2)
            #    driver.find_element_by_xpath(self.Popup).click()
            #    adClicked = True
            driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
            time.sleep(1)
            for quantity in range(self.QuantityList[num]-1):
                driver.find_element_by_xpath('//*[@id="cart"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/button[2]').click()
                time.sleep(1)
        return True

    def login_to_gmail(self, driver):
        try:
            email = ShopInfo.Login["Email"][-1]
            password = ShopInfo.Login["Password"][-1]
            driver.get('http://gmail.com')
            driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email + Keys.ENTER)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password + Keys.ENTER)
            return True
        except:
            print("Error")
            return True

    def checkout(self):
        '''
        phone = ShopInfo.Login["Phone"][-1]
        firstname = ShopInfo.Login["FirstName"][-1]
        lastname = ShopInfo.Login["LastName"][-1]
        address = ShopInfo.Login["Address"][-1]
        city = ShopInfo.Login["City"][-1]
        zipcode = ShopInfo.Login["Zipcode"][-1]
        email = ShopInfo.Login["Email"][-1]
        '''
        # ----- TEST CASES -----
        phone = '562 916 5122'
        firstname = 'carmine'
        lastname = 'choi'
        address = '19611 Jacob Ave'
        city = 'cerritos'
        zipcode = '90703'
        email = 'gangmin5519@gmail.com'
        cardNum = '1234567891234567'
        cardName = 'Ooga Booga'
        cardExp = '06/20'
        cardSecurity = '212'


        driver = webdriver.Chrome('./chromedriver')

        #if not self.login_to_gmail(driver):
        #    return False
        time.sleep(1)
        if not self.testURL(driver):
            print("Cannot Order")
            return False
        time.sleep(1)
        # ADD OTHER OPTIONS TOO
        driver.find_element_by_xpath('//*[@id="cart"]/div/div/div/div[3]/div[2]/div/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(phone)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(firstname)
        driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys(lastname)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(address)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(city)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(zipcode)
        driver.find_element_by_xpath('// *[ @ id = "checkout_email"]').send_keys(email)
        driver.find_element_by_xpath('// *[ @ id = "checkout_buyer_accepts_marketing"]').click()
        time.sleep(7)
        #button = GUI.CaptchaButton()
        #button.showNormal()
        #time.sleep(10)
        #time.sleep(20)
        #driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        # time.sleep(30)
        # driver.close()

        # continue to payment xpath
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div/form/div[2]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div/form/div[2]/button').click()
        # /html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button
        time.sleep(1)
        #card number
        # // *[ @ id = "number"]
        driver.find_element_by_xpath('// *[ @ id = "number"]').send_keys(cardNum)
        # // *[ @ id = "number"]                             //*[@id="card-fields-number-rqtlu1itar900000"]
        # driver.switch_to.frame(0)
        driver.find_element_by_xpath('// *[ @ id = "number"]').send_keys(cardNum)

        #name on card
        # //*[@id="name"]
        driver.find_element_by_xpath('// *[ @ id = "name"]').send_keys(cardName)

        #exp date
        # //*[@id="expiry"]
        driver.find_element_by_xpath('//*[@id="expiry"]').send_keys(cardExp)

        #security code
        # //*[@id="verification_value"]
        driver.find_element_by_xpath('//*[@id="verification_value"]').send_keys(cardSecurity)
        time.sleep(20)
        #complete order button
        # /html/body/div[2]/div/div[1]/div[2]/div/div/form/div[4]/div[1]/button

        # driver.switchTo().defaultContent();

        return driver