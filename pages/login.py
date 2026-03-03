
from selenium.webdriver.common.by import By


import pytest

from selenium.webdriver.support.ui import Select


class LoginPage:
    
    def __init__(self,driver):

        self.driver = driver

        # TC001 locators

        self.Signup_login_btn = (By.XPATH,'//a[@href="/login"]')

        self.Name = (By.NAME,'name')

        self.Email = (By.XPATH,'//input[@data-qa="signup-email"]')

        self.Signup = (By.XPATH,'//button[text()="Signup"]')

        self.id = (By.ID,'id_gender1')

        self.account_user = (By.ID,"name")

        self.password = (By.ID,"password")

        self.days = (By.ID,"days")

        self.months = (By.ID,'months')

        self.years = (By.ID,'years')

        self.checkbox = (By.NAME,"newsletter")

        self.checkbox2 = (By.ID,'optin')

        self.start_name = (By.CSS_SELECTOR,'input[name=first_name]')

        self.ends_name = (By.CSS_SELECTOR,'input[name=last_name]')

        self.working = (By.ID,'company')

        self.working_address = (By.ID,'address1')
        
        self.working_address2 = (By.ID,'address2')

        self.location = (By.ID,'country')

        self.state = (By.ID,'state')

        self.city = (By.ID,'city')

        self.code = (By.CSS_SELECTOR,'input[data-qa=zipcode]')

        self.ph_number = (By.CSS_SELECTOR,'input[id=mobile_number]')

        self.xpath = (By.XPATH,'//button[text()="Create Account"]')

        self.tab = (By.XPATH,'//*[text()="Test Cases"]')


        # TC002 & TC003 locators 
        
        self.login_email = (By.CSS_SELECTOR,'input[data-qa=login-email]')

        self.login_password = (By.CSS_SELECTOR,'input[data-qa=login-password]')

        self.button = (By.CSS_SELECTOR,'button[data-qa=login-button]')

        # TC004 logout Method

        self.logout = (By.XPATH,'//a[@href="/logout"]')


        
        # Signup method
    
    def click_signup_login(self):

        self.driver.find_element(*self.Signup_login_btn).click()
    
    def enter_signup_name(self,name):

        self.driver.find_element(*self.Name).send_keys(name)
    
    def enter_signup_email(self,email):

        self.driver.find_element(*self.Email).send_keys(email)
    
    def click_signup_button(self):

        self.driver.find_element(*self.Signup).click()
    
    #Enter Account Information

    def enter_Title(self):

        self.driver.find_element(*self.id).click()
    
    def create_name(self,user_name):
        
        self.driver.find_element(*self.account_user).send_keys(user_name)
    
    def create_password(self,user_password):

        self.driver.find_element(*self.password).send_keys(user_password)

    
    def select_day(self,days):

        dropdown = Select(self.driver.find_element(*self.days))

        dropdown.select_by_visible_text(days)
    
    def select_month(self,months):

        dropdown = Select(self.driver.find_element(*self.months))

        dropdown.select_by_visible_text(months)
    
    def select_year(self,years):

        dropdown = Select(self.driver.find_element(*self.years))

        dropdown.select_by_visible_text(years)
    
    def click_checkbox(self):
        
        self.driver.find_element(*self.checkbox).click()
    
    def click_checkbox2(self):

        self.driver.find_element(*self.checkbox2).click()
    
    #Address Information

    def first_name(self,starting_name):
        
        self.driver.find_element(*self.start_name).send_keys(starting_name)


    def lost_name(self,end_name):

        self.driver.find_element(*self.ends_name).send_keys(end_name)
    
    def company(self,company_name):

        self.driver.find_element(*self.working).send_keys(company_name)
    
    def enter_address1(self,address):

        self.driver.find_element(*self.working_address).send_keys(address)
    
    def enter_address2(self,address):
        self.driver.find_element(*self.working_address2).send_keys(address)
    
    def country(self,country):

        dropdown2 = Select(self.driver.find_element(*self.location))
        
        dropdown2.select_by_visible_text(country)
    
    def enter_state(self,state):

        self.driver.find_element(*self.state).send_keys(state)
    
    def enter_city(self,city):

        self.driver.find_element(*self.city).send_keys(city)
    
    def enter_zipcode(self,code):

        self.driver.find_element(*self.code).send_keys(code)
    
    def enter_ph_number(self,number):

        self.driver.find_element(*self.ph_number).send_keys(number)
    
    def create_account(self):

        self.driver.find_element(*self.xpath).click()


    # TC002 & TC003 code deployment


    def enter_login_email(self,mail):

        self.driver.find_element(*self.login_email).send_keys(mail)
    
    def enter_login_password(self,password):

        self.driver.find_element(*self.login_password).send_keys(password)
    
    def click_login_button(self):
        
        self.driver.find_element(*self.button).click()

    #TC004 logout website
    
    def click_logout(self):
        
        self.driver.find_element(*self.logout).click()

    
    # TC005 Register User with Existing Email

    def click_signup_existing_email(self):
        
        self.click_signup_button()   

    
    #TC007 checking on the Testcases tab

    def click_test_case_tab(self):

        self.driver.find_element(*self.tab).click()
    
 



        
        



    
  








    

    

    


    

    

    


    
