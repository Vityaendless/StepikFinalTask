from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Refistration form is not presented"

    def register_new_user(self, email, password):
        email_obj = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_obj.send_keys(email)
        password_obj = self.browser.find_element(*LoginPageLocators.PASS)
        password_obj.send_keys(password)
        repeat_password_obj = self.browser.find_element(*LoginPageLocators.REPEAT_PASS)
        repeat_password_obj.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), 'Without a button'
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

    def login_user(self, email, password):
        email_obj = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_obj.send_keys(email)
        password_obj = self.browser.find_element(*LoginPageLocators.PASS)
        password_obj.send_keys(password)
        repeat_password_obj = self.browser.find_element(*LoginPageLocators.REPEAT_PASS)
        repeat_password_obj.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), 'Without a button'
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()