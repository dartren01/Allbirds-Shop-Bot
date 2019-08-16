import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

phone = '562 916 5122'
firstname = 'carmine'
lastname = 'choi'
address = '19611 Jacob Ave'
city = 'cerritos'
zipcode = '90703'

driver = webdriver.Chrome('./chromedriver')
time.sleep(1)
driver.get('https://kith.com/collections/mens-footwear/products/vans-og-style-36-lx-black-marshmallow')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="shopify-section-product"]/section[1]/div[4]/form/button').click()
driver.find_element_by_xpath('//*[@id="cookie__bar"]/div/div[3]/a').click()
#driver.find_element_by_xpath('//*[@id="vans-og-style-36-lx-black-marshmallow"]/div[6]/div/div/div/button').click()
#driver.find_element_by_xpath('//*[@id="shopify-section-header"]/section/header/nav/ul/li[11]/a/svg').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="CartContainer"]/form/div[3]/button').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(phone)
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(firstname)
driver.find_element_by_xpath('// *[ @ id = "checkout_shipping_address_last_name"]').send_keys(lastname)
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(address)
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(city)
driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(zipcode)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys('dartren@gmail.com')

