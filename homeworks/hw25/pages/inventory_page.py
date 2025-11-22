from playwright.sync_api import expect
from homeworks.hw25.pages.base_page import BasePage


class InventoryPage(BasePage):
    add_backpack_button = 'button[id="add-to-cart-sauce-labs-backpack"]'
    cart_badge = '[class=shopping_cart_badge]'
    cart_link = '[class=shopping_cart_link]'
    menu_button = 'button[id="react-burger-menu-btn"]'
    logout_link = '[id="logout_sidebar_link"]'

    def verify_page_loaded(self):
        self.expect_url(r'.*/inventory\.html')
        self.expect_title('Products')

    def add_backpack_to_cart(self):
        self.page.click(self.add_backpack_button)
        expect(self.page.locator(self.cart_badge)).to_have_text('1')

    def go_to_cart(self):
        self.page.click(self.cart_link)

    def logout(self):
        self.page.click(self.menu_button)
        self.page.click(self.logout_link)
