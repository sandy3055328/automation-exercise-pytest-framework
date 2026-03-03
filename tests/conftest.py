 
from selenium import webdriver


import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='Chrome', help='browser_selection')


@pytest.fixture()

def browser_setup(request):

    browser = request.config.getoption("--browser") #both will work browser

    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Browser was founded")

    elif browser == "Edge":
        
        driver = webdriver.Edge()
        print("Browser was founded")
    else:
        print("No Browser founded")

        pytest.skip("Brower not supported")
    
    driver.maximize_window()

    driver.implicitly_wait(10)

    yield driver

    driver.quit()