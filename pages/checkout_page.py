
from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self,driver):

        self.driver = driver

        self.proceed = (By.XPATH,"//*[text()='Proceed To Checkout']")

        self.total_amount = (By.XPATH,"//*[text()='Total Amount']")

        self.payment = (By.XPATH,"//*[@class='cart_total_price']")

        self.submit = (By.XPATH,"//*[text()='Place Order']")

        self.name_of_card = (By.NAME,'name_on_card')

        self.card_name = (By.NAME,'card_number')  

        self.cvc = (By.NAME,'cvc') 

        self.Expiration = (By.NAME,'expiry_month')

        self.year = (By.NAME,'expiry_year')

        self.confirm_order = (By.ID,'submit')

        self.confirm_text = (By.XPATH,"//div[@class='alert-success alert']")

        self.button = (By.XPATH,"//*[text()='Pay and Confirm Order']")

        self.confirm_placed = (By.XPATH,"//*[text()='Order Placed!']")

        self.confirm_message = (By.XPATH,"//*[text()='Congratulations! Your order has been confirmed!']")

    

    def click_proceed_to_checkout(self):

        self.driver.find_element(*self.proceed).click()
    
    def print_text(self):

        return self.driver.find_element(*self.total_amount).text
    
    def print_amount(self):

        return self.driver.find_element(*self.payment).text
    
    def click_place_order_button(self):

        self.driver.find_element(*self.submit).click()
    
    def enter_name_of_card(self,name):

        self.driver.find_element(*self.name_of_card).send_keys(name)
    

    def enter_card_name(self,card):

        self.driver.find_element(*self.card_name).send_keys(card)
    
    
    def enter_cvc(self, cvc):
        
        self.driver.find_element(*self.cvc).send_keys(cvc)

    
    def enter_expiration_month(self,month):

         self.driver.find_element(*self.Expiration).send_keys(month)

    def enter_year(self,year):

         self.driver.find_element(*self.year).send_keys(year)
    
    def click_confirm_order_button(self):

         self.driver.find_element(*self.confirm_order).click()
        
    
    def confirm_text_message(self):
        
        return self.driver.find_element(*self.confirm_text).text
    
    def confirm_button(self):

        self.driver.find_element(*self.button).click()
    
    def confirm_order_placed(self):

        return self.driver.find_element(*self.confirm_placed).text
    
    def confirmation_message(self):

        return self.driver.find_element(*self.confirm_message).text




    



    


     

    
    




