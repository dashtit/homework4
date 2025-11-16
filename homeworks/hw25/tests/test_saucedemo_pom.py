from homeworks.hw25.pages.login_page import LoginPage
from homeworks.hw25.pages.inventory_page import InventoryPage
from homeworks.hw25.pages.cart_page import CartPage
from homeworks.hw25.pages.checkout_page import CheckoutPage
from homeworks.hw25.pages.checkout_complete_page import CheckoutCompletePage
from homeworks.hw25.utilities.users import User


class TestSauceDemoPOM:

    def test_full_purchase_flow(self, browser_page):
        login_page = LoginPage(browser_page)
        inventory_page = InventoryPage(browser_page)
        cart_page = CartPage(browser_page)
        checkout_page = CheckoutPage(browser_page)
        complete_page = CheckoutCompletePage(browser_page)
        login_page.open_login_page()
        login_page.login(User.STANDARD_USER, User.USER_PASSWORD)
        inventory_page.verify_page_loaded()
        inventory_page.add_backpack_to_cart()
        inventory_page.go_to_cart()
        cart_page.verify_cart_page()
        cart_page.proceed_to_checkout()
        checkout_page.verify_checkout_step_one()
        checkout_page.fill_customer_info(User.FIRSTNAME, User.LASTNAME, User.ZIPCODE)
        checkout_page.verify_checkout_step_two()
        checkout_page.finish_checkout()
        complete_page.verify_checkout_complete()
        complete_page.back_to_products()
        inventory_page.logout()
