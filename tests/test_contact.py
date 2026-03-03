
import pytest

import time

from pages.contact_page import Contactdetails


def test_contact(browser_setup):

    # 1. Navigate to the homepage
    # 2. Create ContactPage object
    # 3. Perform all actions (click, fill, upload)
    # 4. Handle the browser alert/popup after submit
    # 5. Verify the success message appears

    driver = browser_setup

    driver.get("https://automationexercise.com/signup")
    
    contact = Contactdetails(driver)

    contact.click_contact_us_login()

    contact.enter_customer_name("lawrence")

    contact.enter_customer_email("testuser13@test.com")

    contact.enter_customer_subject("unble to login account")

    contact.enter_customer_query("unble to login account")

    contact.enter_customer_doc("D://D Downloads//deepseek_text_20260302_94868d.txt")

    contact.click_on_submit_button()

    contact.handle_success_alert()

    assert "Success! Your details have been submitted successfully." in driver.page_source
