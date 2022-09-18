from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    skip_button = ("id", "com.reddit.frontpage:id/skip_button")

    def skip_registration(self):
        self.wait.until(EC.element_to_be_clickable(self.get_element(self.skip_button)))
        self.get_element(self.skip_button).click()
        return self
