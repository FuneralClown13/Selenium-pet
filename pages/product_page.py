from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def open(self):
        self.browser.get(self.url)

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

    def get_alerts(self):
        return self.browser.find_elements(*ProductPageLocators.ALERTS)

    def check_name(self):
        return self.get_product_name().text == self.get_alerts()[0].text

    def check_price(self):
        return self.get_product_price().text == self.get_alerts()[2].text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def should_disappeared_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
