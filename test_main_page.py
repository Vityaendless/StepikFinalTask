from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link_of_login_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

    reg_or_login_page = LoginPage(browser, link_of_login_page)
    reg_or_login_page.should_be_login_page()