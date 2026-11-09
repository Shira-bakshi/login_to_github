from playwright.sync_api import Page
from utilities import config


class BasePage:
    PATH = "/"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto(config.GITHUB_URL)
        self.page.pause()  # רק כדי לראות את הדף, אפשר למחוק אחר כך

    def wait_for_url(self, url: str) -> None:
        self.page.wait_for_url(url)