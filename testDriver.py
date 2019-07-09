import time
from selenium import webdriver

class testDriver:
    def __init__(self, UrlList, PopUp, FinalProductList):
        self.urls = UrlList
        self.Popup = PopUp
        self.FinalProdList = FinalProductList

    def testURL(self, driver):
        # Some urls have contact to order
        adClicked = False
        for num in range(len(self.urls)):
            driver.get(self.urls[num])
            if (not adClicked):
                time.sleep(3)
                driver.find_element_by_xpath(self.Popup).click()
                adClicked = True

            for item in self.FinalProdList[num]['tags']:
                if (item == 'email-orders' or item == 'phone-orders'):
                    print("This is a contact to order")
                    return False
            driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
        return True

    def checkout(self):
        driver = webdriver.Chrome('./chromedriver')
        if(not self.testURL(driver)):
            print("Cannot Order")
            return False

        # STORE THESE IN A SEPARATE FILE (MODULARIZE). ADD OTHER OPTIONS TOO
        time.sleep(1)
        driver.find_element_by_xpath('// *[ @ id = "CartContainer"] / form / div[2] / button').click()

        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('12345678910')
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')
        driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys('Lim')
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('12345 Burger Dr.')
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Cerritos')
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('90703')
        driver.find_element_by_xpath('// *[ @ id = "checkout_email"]').send_keys('dartren@gmail.com')

        #driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        time.sleep(30)
        driver.close()