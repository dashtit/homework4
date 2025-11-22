from playwright.sync_api import expect
from homeworks.hw25.pages.base_page import BasePage


class CheckoutPage(BasePage):
    first_name = 'input[id="first-name"]'
    last_name = 'input[id="last-name"]'
    postal_code = 'input[id="postal-code"]'
    continue_button = 'input[id="continue"]'
    finish_button = 'button[id="finish"]'

    def verify_checkout_step_one(self):
        self.expect_url(r'.*/checkout-step-one\.html')
        self.expect_title('Checkout: Your Information')

    def fill_customer_info(self, first, last, zip_code):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, zip_code)
        expect(self.page.locator(self.first_name)).to_have_value(first)
        expect(self.page.locator(self.last_name)).to_have_value(last)
        expect(self.page.locator(self.postal_code)).to_have_value(zip_code)
        self.page.click(self.continue_button)

    def verify_checkout_step_two(self):
        self.expect_url(r'.*/checkout-step-two\.html')
        self.expect_title('Checkout: Overview')
        expect(self.page.locator('.cart_quantity')).to_have_text('1')
        expect(self.page.locator('.inventory_item_name')).to_have_text('Sauce Labs Backpack')

    def finish_checkout(self):
        self.page.click(self.finish_button)
