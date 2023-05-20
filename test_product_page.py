from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
import time


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_element_present(*BasePageLocators.BASKET_HEADER_BUTTON), 'Without a basket button'
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    time.sleep(20)
    basket_page.should_be_text_about_empty_basket()