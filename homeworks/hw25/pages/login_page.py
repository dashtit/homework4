from playwright.sync_api import expect
from homeworks.hw25.pages.base_page import BasePage


class LoginPage(BasePage):
    username_field = 'input[id="user-name"]'
    password_field = 'input[id="password"]'
    login_button = 'input[id="login-button"]'

    def open_login_page(self):
        self.open('https://www.saucedemo.com/')

    def login(self, username: str, password: str):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        expect(self.page.locator(self.username_field)).to_have_value(username)
        expect(self.page.locator(self.password_field)).to_have_value(password)
        self.page.click(self.login_button)
