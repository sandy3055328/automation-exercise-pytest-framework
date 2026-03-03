 
import time

from pages.products_page import ProductsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # ← ADD THIS
import time

import pytest

@pytest.mark.skip
def test_click_product_tab(browser_setup):
    driver = browser_setup
    driver.get("https://automationexercise.com")

    products = ProductsPage(driver)

    products.close_popup()

    products.click_products_tab()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/products")
    )

    assert "/products" in driver.current_url

    #assert "products" in driver.current_url

@pytest.mark.tc009

def test_search_product(browser_setup):
    
    driver = browser_setup
    driver.get("https://automationexercise.com")

    products_searching = ProductsPage(driver)
    products_searching.search_product("T-shirt")
    products_searching.search_button()

    
    assert "T-shirt" in driver.current_url


@pytest.mark.tc010

def test_homepage_subscription(browser_setup):
    
    driver = browser_setup
    driver.get("https://automationexercise.com")

    membership = ProductsPage(driver)
    membership.subscription()
    membership.subscription_email("testcas@123.com")
    time.sleep(5)

    assert "successfully subscribed" in driver.page_source

@pytest.mark.tc011

def test_cart_subscription(browser_setup):
    
    driver = browser_setup
    driver.get("https://automationexercise.com")

    check_subscription_cart = ProductsPage(driver)
    check_subscription_cart.check_cart()
    check_subscription_cart.enter_email("testcas@123.com")
    time.sleep(5)


@pytest.mark.tc012

def test_add_to_cart(browser_setup):
    
    driver = browser_setup
    driver.get("https://automationexercise.com")

    add_product = ProductsPage(driver)
    add_product.add_product_by_index(0)
    add_product.get_confirmation_message()
    
    assert "Your product has been added to cart." in driver.page_source

@pytest.mark.tc013

def test_verify_cart_quantity(browser_setup):
    
    driver = browser_setup
    driver.get("https://automationexercise.com")

    products = ProductsPage(driver)
    products.go_to_cart()
    products.get_product_quantity()
    products.get_product_name()
    
    assert "GRAPHIC DESIGN MEN T SHIRT - BLUE" in driver.page_source
    
    assert products.get_product_quantity() == "1"






