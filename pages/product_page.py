from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_to_basket_correct(self):
        self.button_click(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        self.should_be_correct_massage_add_to_basket()
        self.should_be_correct_summ_in_basket()


    def should_be_correct_massage_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text,\
        "In basked added a wrong product"


    def should_be_correct_summ_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text,\
        "Wrong sum of basket"

