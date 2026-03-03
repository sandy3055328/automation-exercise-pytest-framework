 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

class ProductsPage:
    def __init__(self, driver):

        self.driver = driver

        self.products_tab = (By.XPATH, "//a[text()=' Products']")  # Note the space!

        self.search = (By.NAME,'search')

        self.button = (By.ID,'submit_search')

        self.email = (By.ID,'susbscribe_email')

        self.cart = (By.XPATH,'//*[text()=" Cart"]')

        self.xpath = (By.XPATH,'//input[@type="email"]')

        self.submit = (By.XPATH,'//button[@type="submit"]')

        self.add_to_cart = (By.XPATH,"//*[text()='Add to cart']")

        self.confirm_msg =  (By.XPATH,"//*[text()='Your product has been added to cart.']")

        self.view_cart = (By.XPATH,'//*[text()="View Cart"]')

        self.quantity_display = (By.XPATH,'//button[@class="disabled"]')

        self.name = (By.XPATH,"//*[text()='GRAPHIC DESIGN MEN T SHIRT - BLUE']")

        self.close_popup_locator = (By.XPATH, "//button[contains(text(),'Close')] | //div[@class='close']")
    
    def close_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.close_popup_locator)
            )
            close_button.click()
            time.sleep(1)
            print("Popup closed successfully")
        except:
            print("No popup to close or couldn't close it")
            pass

    def click_products_tab(self):
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.products_tab)).click()
        
        print("Products tab clicked.")  
    
    
    
    def subscription(self):
        
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    

    def search_button(self):

        self.driver.find_element(*self.button).click()
    
    
    def subscription_email(self,email):

        self.driver.find_element(*self.email).send_keys(email)

    
    def check_cart(self):

        self.driver.find_element(*self.cart).click()
    
    def enter_email(self,email):

        self.driver.find_element(*self.xpath).send_keys(email)
    
    def click_submit_button(self):
        
        self.driver.find_element(*self.submit).click()

    
    def add_product_by_index(self,index):
        
        add_button = self.driver.find_elements(*self.add_to_cart)

        add_button[index].click()

    def get_confirmation_message(self):
        
        return self.driver.find_element(*self.confirm_msg).text
    
    def go_to_cart(self):

        self.driver.find_element(*self.view_cart).click()
    
    def get_product_quantity(self):

        return self.driver.find_element(*self.quantity_display).text

    def get_product_name(self):

        return self.driver.find_element(*self.name).text
    
    

    

