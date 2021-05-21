from UIElement import UIElement as Element
from selenium.webdriver.common.by import By

# May 20th, 2021
# student Evgeny Abdulin

class Footer:
    def __init__(self, browser):
        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Information')]")
        self.about_us = Element(browser, By.XPATH, "//a[contains(text(),'About Us')]")
        self.delivery_info = Element(browser, By.XPATH, "//a[contains(text(),'Delivery Information')]")
        self.privacy_policy = Element(browser, By.XPATH, "//a[contains(text(),'Privacy Policy')]")
        self.terms_conditions = Element(browser, By.XPATH, "//a[contains(text(),'Terms & Conditions')]")

        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Customer Service')]")
        self.contact_us = Element(browser, By.XPATH, "//a[contains(text(),'Contact Us')]")
        self.returns = Element(browser, By.XPATH, "//a[contains(text(),'Returns')]")
        self.site_map = Element(browser, By.XPATH, "//a[contains(text(),'Site Map')]")

        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Extras')]")
        self.brands = Element(browser, By.XPATH, "//a[contains(text(),'Brands')]")
        self.gift_certificates = Element(browser, By.XPATH, "//a[contains(text(),'Gift Certificates')]")
        self.affiliates = Element(browser, By.XPATH, "//a[contains(text(),'Affiliates')]")
        
        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'My Account')]")
        self.my_account = Element(browser, By.XPATH, "//a[contains(text(),'My Account')]")
        self.order_history = Element(browser, By.XPATH, "//a[contains(text(),'Order History')]")
        self.wish_list = Element(browser, By.XPATH, "//a[contains(text(),'Wish List')]")
        self.newsletter = Element(browser, By.XPATH, "//a[contains(text(),'Newsletter')]")

        self.opencart_ext_link = Element(browser, By.XPATH, "//a[contains(text(),'OpenCart')]")


    def click_about_us(self):
        self.about_us.click()

