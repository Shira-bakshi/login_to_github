# TEST LOGIN GITHUB
import re
from pages import login_page
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utilities import config


def test_login_github(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_sign_in()
    login_page.wait_for_login_page()
    expect(page).to_have_url(re.compile(r".*/login"))

    login_page.login(config.EMAIL_GITHUB, config.PASSWORD_GITHUB)

    expect(page).not_to_have_url(re.compile(r".*/login"))

    page.wait_for_timeout(5000)  # רק כדי לראות, אפשר למחוק

def test_login_with_wrong_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.click_sign_in()
    login_page.wait_for_login_page()

    login_page.login(config.EMAIL_GITHUB, "wrong_password_123")

    expect(login_page.get_error_message()).to_be_visible()