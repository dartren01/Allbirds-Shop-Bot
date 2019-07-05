from selenium import webdriver
import time
driver = webdriver.Chrome('./chromedriver')
driver.get('https://packershoes.com/collections/new-arrivals/products/adidas-rivalry-hi-keith-haring?variant=21876300349529')
driver.find_element_by_xpath('//*[@id="AddToCart--product-packer-template"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="adidas-originals-rivalry-hi-quot-keith-haring-quot"]/div[7]/div/div/div/button/img').click()
driver.find_element_by_xpath('//*[@id="CartContainer"]/form/div[2]/button').click()


driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys('Darren')
