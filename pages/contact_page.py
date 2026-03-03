
from selenium.webdriver.common.by import By
class Contactdetails:

    def __init__(self,driver):
        
        self.driver = driver

        self.xpath = (By.XPATH,'//*[@href="/contact_us"]')

        self.name = (By.NAME,'name')

        self.email = (By.NAME,'email')

        self.subject = (By.NAME,'subject')

        self.message = (By.ID,'message')

        self.file = (By.NAME,'upload_file')

        self.submit = (By.NAME,'submit')


    
    def click_contact_us_login(self):

        self.driver.find_element(*self.xpath).click()

    def enter_customer_name(self,name):

        self.driver.find_element(*self.name).send_keys(name)

    def enter_customer_email(self,email):

        self.driver.find_element(*self.email).send_keys(email)

    def enter_customer_subject(self,subject):

        self.driver.find_element(*self.subject).send_keys(subject)
    
    def enter_customer_query(self,query):

        self.driver.find_element(*self.message).send_keys(query)
    
    def enter_customer_doc(self,file):

        self.driver.find_element(*self.file).send_keys(file)
    
    def click_on_submit_button(self):
        
        self.driver.find_element(*self.submit).click()
    
    def handle_success_alert(self):

        alert = self.driver.switch_to.alert

        alert_test = alert.text

        alert.accept()

        return alert_test




    
    

    

