from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY_FORM) , "Product form is presented"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Text about empty basket not found"