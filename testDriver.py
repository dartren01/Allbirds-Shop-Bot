import time
from selenium import webdriver
import ShopInfo
import GUI


class testDriver:
    def __init__(self, UrlList, FinalProductList, QuantityList):
        self.urls = UrlList
        self.FinalProdList = FinalProductList
        self.QuantityList = QuantityList

    def testURL(self, driver):
        for num in range(len(self.urls)):
            driver.get(self.urls[num])
            driver.find_element_by_xpath('//*[@id="add-to-cart"]').click()
            time.sleep(1)
            for quantity in range(self.QuantityList[num]-1):
                driver.find_element_by_xpath('//*[@id="cart"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/button[2]').click()
                time.sleep(1)
        return True

    def checkout(self):
        try:
            firstname = ShopInfo.Login["FirstName"][-1]
            lastname = ShopInfo.Login["LastName"][-1]
            address = ShopInfo.Login["Address"][-1]
            city = ShopInfo.Login["City"][-1]
            zipcode = ShopInfo.Login["Zipcode"][-1]
            email = ShopInfo.Login["Email"][-1]
        except:
            errorMsg = GUI.MessageBox(True)
            errorMsg.done(1)
            return 1

        driver = webdriver.Chrome('./chromedriver')

        if not self.testURL(driver):
            return False

        time.sleep(1)
        # ADD OTHER OPTIONS TOO
        driver.find_element_by_xpath('//*[@id="cart"]/div/div/div/div[3]/div[2]/div/a').click()
        time.sleep(1)

        # INFORMATION PAGE
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(firstname)
        driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys(lastname)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(address)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(city)
        driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(zipcode)
        driver.find_element_by_xpath('// *[ @ id = "checkout_email"]').send_keys(email)
        driver.find_element_by_xpath('// *[ @ id = "checkout_buyer_accepts_marketing"]').click()
        time.sleep(5)

        # SHIPPING PAGE
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div/form/div[2]/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div/form/div[2]/button').click()

        # PAYMENT PAGE
        time.sleep(1)

        button = GUI.MessageBox(False)
        button.done(1)

        driver.quit()
        return 0
