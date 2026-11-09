# login_page.py
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def click_sign_in(self) -> None:
        self.page.get_by_role("link", name="Sign in").first.click()

    def wait_for_login_page(self) -> None:
        self.wait_for_url("**/login")

    def get_username_input(self):
        return self.page.get_by_role("textbox", name="Username or email address")

    def get_password_input(self):
        return self.page.get_by_role("textbox", name="Password")

    def get_sign_in_button(self):
        return self.page.get_by_role("button", name="Sign in", exact=True)

    def click_sign_in_button(self) -> None:
        self.get_sign_in_button().click()

    def login(self, username: str, password: str) -> None:
        self.get_username_input().fill(username)
        self.get_password_input().fill(password)
        self.click_sign_in_button()