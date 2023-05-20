from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_HEADER_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")

class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong:nth-child(1)")

class BasketPageLocators():
    BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, "#content_inner .basket_summary")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")