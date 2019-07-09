import time

class testDriver:
    def __init__(self, UrlList, PopUp, FinalProductList, driver):
        self.urls = UrlList
        self.Popup = PopUp
        self.FinalProdList = FinalProductList
        self.driver = driver

    def testURL(self):
        # Some urls have contact to order
        adClicked = False
        for num in range(len(self.urls)):
            self.driver.get(self.urls[num])
            if (not adClicked):
                time.sleep(3)
                self.driver.find_element_by_xpath(self.Popup).click()
                adClicked = True

            for item in self.FinalProdList[num]['tags']:
                if (item == 'email-orders' or item == 'phone-orders'):
                    print("This is a contact to order")
                    return False
            self.driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
        return True

    def checkout(self):
        if(not self.testURL()):
            print("Cannot Order")
            return False

        # STORE THESE IN A SEPARATE FILE (MODULARIZE). ADD OTHER OPTIONS TOO
        time.sleep(1)
        self.driver.find_element_by_xpath('// *[ @ id = "CartContainer"] / form / div[2] / button').click()

        self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys('12345678910')
        self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')
        self.driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys('Lim')
        self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys('12345 Burger Dr.')
        self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys('Cerritos')
        self.driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys('90703')
        self.driver.find_element_by_xpath('// *[ @ id = "checkout_email"]').send_keys('dartren@gmail.com')

        #driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        time.sleep(30)