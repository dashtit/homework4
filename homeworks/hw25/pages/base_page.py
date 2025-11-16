from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def expect_url(self, url: str):
        expect(self.page).to_have_url(url)

    def expect_title(self, text: str):
        expect(self.page.locator('[class=title]')).to_have_text(text)
