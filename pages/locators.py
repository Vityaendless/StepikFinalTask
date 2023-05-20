from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_HEADER_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PARAMETERS = (By.CSS_SELECTOR, ".alertinner strong")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    PASS = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REPEAT_PASS = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")
    ENTER_EMAIL = (By.CSS_SELECTOR, ".login_form #id_login-username")
    ENTER_PASS = (By.CSS_SELECTOR, ".login_form #id_login-password")
    ENTER_BUTTON = (By.NAME, "login_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong:nth-child(1)")

class BasketPageLocators():
    BASKET_SUMMARY_FORM = (By.CSS_SELECTOR, "#content_inner .basket_summary")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")