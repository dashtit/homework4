from playwright.sync_api import expect
from homeworks.hw25.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    back_to_products_button = 'button[id="back-to-products"]'

    def verify_checkout_complete(self):
        self.expect_url(r'.*/checkout-complete\.html')
        self.expect_title('Checkout: Complete!')
        (expect(self.page.locator('[class=complete-header]')).
         to_have_text('Thank you for your order!'))

    def back_to_products(self):
        self.page.click(self.back_to_products_button)
        self.expect_url(r'.*/inventory\.html')
        self.expect_title('Products')
        expect(self.page.locator('[class=shopping_cart_badge]')).to_be_hidden()
