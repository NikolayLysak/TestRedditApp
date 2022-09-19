from appium.webdriver.common.appiumby import AppiumBy

from src.pages.base_page import Base


class LoginPage(Base):
    progress_bar = (AppiumBy.ID, "com.reddit.frontpage:id/progress_bar")
    welcome_banner = (AppiumBy.ID, "com.reddit.frontpage:id/welcome_snoo")
    skip_button = (AppiumBy.ID, "com.reddit.frontpage:id/skip_button")

    def skip_registration(self):
        self.wait_element_be_disabled(self.progress_bar)
        self.wait_element_be_enabled(self.welcome_banner)
        self.clic_by_element(self.skip_button)
