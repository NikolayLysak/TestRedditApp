from appium.webdriver.common.appiumby import AppiumBy

from src.pages.base_page import Base
from retry import retry
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage(Base):
    progress_bar = (AppiumBy.ID, "com.reddit.frontpage:id/progress_bar")
    welcome_banner = (AppiumBy.ID, "com.reddit.frontpage:id/welcome_snoo")
    skip_button = (AppiumBy.ID, "com.reddit.frontpage:id/skip_button")

    @retry(TimeoutException, 3, 1)
    def skip_registration(self):
        self.wait_element_be_disabled(self.progress_bar)
        self.clic_by_element(self.skip_button)
        self.wait_element_be_disabled(self.welcome_banner)
