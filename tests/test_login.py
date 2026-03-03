"""
Test Suite: Login Functionality
Website: Automation Exercise
"""

import pytest
from pages.login import LoginPage

import time


# =============================================
# TC001: Register User
# =============================================

@pytest.mark.tc001

def test_register_user(browser_setup):

    """
    Test Case ID: TC001
    Description: Register a new user
    Steps:
    1. Navigate to website
    2. Click on Signup/Login button
    3. Enter name and email
    4. Click Signup button
    5. Fill account details
    6. Click Create Account
    7. Verify account created
    """

    driver = browser_setup

    driver.get("https://automationexercise.com/login")

    login = LoginPage(driver)

    # Steps 2-4: Signup

    login.click_signup_login()

    login.enter_signup_name("TestUser")

    login.enter_signup_email("testuser16@test.com")

    login.click_signup_button()

    
    # Step 5: Fill account details 

    login.enter_Title()

    login.create_name("Lawrence")

    login.create_password("1234567890")

    login.select_day("29")

    login.select_month("January")

    login.select_year("1999")

    login.click_checkbox()

    login.click_checkbox2()

    # Address Information

    login.first_name("lawrence")

    login.lost_name('raghav')

    login.company("IBM")

    login.enter_address1("15 Ashford Lane")

    login.enter_city("Manchester")
    
    login.enter_zipcode("M1 4BT")
    
    login.country("United States")

    login.enter_state("tamil nadu")
    
    login.enter_ph_number("0000000000")

    # Step 6: Click Create Account

    login.create_account()

    # Step 7: Verify account created

    time.sleep(5)

    assert "Account Created!" in driver.page_source


# =============================================
# TC002: Login with Valid Credentials
# =============================================

@pytest.mark.tc002

def test_valid_login(browser_setup):

    """
    Test Case ID: TC002
    Description: Login with correct email and password
    Steps:
    1. Navigate to website
    2. Click on Signup/Login button
    3. Enter valid email and password
    4. Click Login button
    5. Verify logged in successfully
    """

    driver = browser_setup

    driver.get("https://automationexercise.com/login")

    login = LoginPage(driver)

    # Steps 2-4: Login

    login.enter_login_email("testuser13@test.com")

    login.enter_login_password("1234567890")

    login.click_login_button()

    time.sleep(3)

    assert "Logged in as" in driver.page_source


# =============================================
# TC003: Login with InValid Credentials
# =============================================

@pytest.mark.tc003

def test_invalid_login(browser_setup):

     """
    Test Case ID: TC003
    Description: Login with incorrect email and password
    Steps:
    1. Navigate to website
    2. Click on Signup/Login button
    3. Enter invalid email and password
    4. Click Login button
    5. Verify error message appears
    """
     
     driver = browser_setup

     driver.get("https://automationexercise.com/login")

     login = LoginPage(driver)

    # Steps 2-4: Login
     
     login.enter_login_email("wrong13@test.com")
     
     login.enter_login_password("1234567")
     
     login.click_login_button()

     time.sleep(3)
     
     assert "Your email or password is incorrect!" in driver.page_source

# =============================================
# TC004: Logout with Valid Credentials
# =============================================

@pytest.mark.tc004
def test_logout(browser_setup):
    
    """
    Test Case ID: TC004
    Description: Logout user
    Steps:
    1. Navigate to website
    2. Login with valid credentials
    3. Click Logout button
    4. Verify user is redirected to login page
    """
    
    driver = browser_setup

    driver.get("https://automationexercise.com/login")

    login = LoginPage(driver)

    # Steps 2: Login

    login.enter_login_email("testuser13@test.com")

    login.enter_login_password("1234567890")

    login.click_login_button()

    #step 3: Click Logout button

    login.click_logout()

    #step 4 : Verify user is redirected to login page

    assert "Login to your account" in driver.page_source


# =============================================
# TC005: Login with Existing_Email Credentials
# =============================================

@pytest.mark.tc005

def test_existing_email(browser_setup):

    """
    Test Case ID: TC005
    Description: Register User with existing email
    Steps:
    1. Navigate to website
    2. Click on Signup/Login button
    3. Enter name and already registered email
    4. Click Signup button
    5. Verify error message appears
    """
    driver = browser_setup

    driver.get("https://automationexercise.com/login")

    login = LoginPage(driver)

    # step 1-3 : Signup/Login Button

    login.click_signup_login()

    login.enter_signup_name("TestUser")

    login.enter_signup_email("testuser15@test.com")

    #step 4 : Click Signup button

    login.click_signup_existing_email()

    #step 5 :Verify error message appears

    assert "Email Address already exist!" in driver.page_source


# =============================================
# TC007: verifying Test_case TAB
# =============================================

@pytest.mark.tc007

def test_click_test_case_tab(browser_setup):

    driver = browser_setup
    
    """
    Test Case ID: TC007
    Description: Verify Test Cases Page
    Steps:
    1. Navigate to website
    2. Click on 'Test Cases' button
    3. Verify user is navigated to test cases page successfully
    """


    driver.get("https://automationexercise.com")

    login = LoginPage(driver)
    
    login.click_test_case_tab()

    assert "test_cases" in driver.page_source











