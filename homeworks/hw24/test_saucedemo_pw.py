from playwright.sync_api import sync_playwright, expect
import pytest


class TestSauceDemo:

    @pytest.fixture(scope='class')
    def browser_page(self):
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.saucedemo.com/')
        yield page
        browser.close()
        playwright.stop()

    def test_login(self, browser_page):
        browser_page.locator('input[id="user-name"]').fill('standard_user')
        browser_page.locator('input[id="password"]').fill('secret_sauce')
        expect(browser_page.locator('input[id="user-name"]')).to_have_value('standard_user')
        expect(browser_page.locator('input[id="password"]')).to_have_value('secret_sauce')
        browser_page.locator('input[id="login-button"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/inventory.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Products')

    def test_add_to_cart(self, browser_page):
        browser_page.locator('button[id="add-to-cart-sauce-labs-backpack"]').click()
        expect(browser_page.locator('[class=shopping_cart_badge]')).to_have_text('1')

    def test_go_to_cart(self, browser_page):
        browser_page.locator('[class=shopping_cart_link]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/cart.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Your Cart')
        expect(browser_page.locator('[class=cart_quantity]')).to_have_text('1')
        (expect(browser_page.locator('[class=inventory_item_name]'))
         .to_have_text('Sauce Labs Backpack'))

    def test_checkout_step_one(self, browser_page):
        browser_page.locator('button[id="checkout"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Checkout: Your Information')

    def test_checkout_step_two(self, browser_page):
        browser_page.locator('input[id="first-name"]').fill('Umpa')
        browser_page.locator('input[id="last-name"]').fill('Lumpa')
        browser_page.locator('input[id="postal-code"]').fill('123456')
        expect(browser_page.locator('input[id="first-name"]')).to_have_value('Umpa')
        expect(browser_page.locator('input[id="last-name"]')).to_have_value('Lumpa')
        expect(browser_page.locator('input[id="postal-code"]')).to_have_value('123456')
        browser_page.locator('input[id="continue"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Checkout: Overview')
        expect(browser_page.locator('[class=cart_quantity]')).to_have_text('1')
        (expect(browser_page.locator('[class=inventory_item_name]')).
         to_have_text('Sauce Labs Backpack'))

    def test_checkout_complete(self, browser_page):
        browser_page.locator('button[id="finish"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/checkout-complete.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Checkout: Complete!')
        (expect(browser_page.locator('[class=complete-header]')).
         to_have_text('Thank you for your order!'))

    def test_back_home_button(self, browser_page):
        browser_page.locator('button[id="back-to-products"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/inventory.html')
        expect(browser_page.locator('[class=title]')).to_have_text('Products')
        expect(browser_page.locator('[class=shopping_cart_badge]')).to_be_hidden()

    def test_logout_button(self, browser_page):
        browser_page.locator('button[id="react-burger-menu-btn"]').click()
        browser_page.locator('[id="logout_sidebar_link"]').click()
        expect(browser_page).to_have_url('https://www.saucedemo.com/')
