from playwright.sync_api import expect
from homeworks.hw25.pages.base_page import BasePage


class CartPage(BasePage):
    checkout_button = 'button[id="checkout"]'

    def verify_cart_page(self):
        self.expect_url(r'.*/cart\.html')
        self.expect_title('Your Cart')
        expect(self.page.locator('[class=cart_quantity]')).to_have_text('1')
        expect(self.page.locator('[class=inventory_item_name]')).to_have_text('Sauce Labs Backpack')

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
