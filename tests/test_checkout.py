 
from pages.products_page import ProductsPage
from pages.checkout_page import Checkout


def test_checkout(browser_setup):

    driver = browser_setup

    driver.get("https://automationexercise.com")

    # Step 1: Add product to cart
    products = ProductsPage(driver)
    products.add_product_by_index(0)
    products.go_to_cart()

     # Step 2: Now use Checkout page

    checkout = Checkout(driver)

    checkout.click_proceed_to_checkout()

    checkout.print_text()

    print(checkout.print_text())

    checkout.print_amount()

    print(checkout.print_amount())

    checkout.click_place_order_button()

    checkout.enter_name_of_card("Lawrence")

    checkout.enter_card_name("sbi_card")
    
    checkout.enter_cvc("603")
    
    checkout.enter_expiration_month("12")

    checkout.enter_year("2029")

    checkout.click_confirm_order_button()

    checkout.confirm_text_message()

    print(checkout.confirm_text_message())

    checkout.confirm_button()

    checkout.confirm_order_placed()

    print(checkout.confirm_order_placed())

    checkout.confirmation_message()

    print(checkout.confirmation_message())

    assert "Order Placed!" in driver.page_source
    assert "Congratulations" in driver.page_source
    


        
    
    
    




    

