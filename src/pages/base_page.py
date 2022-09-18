from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    driver: WebDriver
    wait: WebDriverWait

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_element(self, locator: tuple) -> WebElement:
        method = locator[0]
        value = locator[1]

        if method == "id":
            return self.driver.find_element(AppiumBy.ID, value)
        elif method == "xpath":
            return self.driver.find_element(AppiumBy.XPATH, value)
        elif method == "accessibility_id":
            return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, value)
        else:
            raise Exception("Invalid locator method.")

    def get_elements(self, locator: tuple) -> list[WebElement]:
        method = locator[0]
        value = locator[1]

        if method == "id":
            return self.driver.find_elements(AppiumBy.ID, value)
        elif method == "xpath":
            return self.driver.find_elements(AppiumBy.XPATH, value)
        elif method == "accessibility_id":
            return self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, value)
        else:
            raise Exception("Invalid locator method.")

    def swipe_element(self, loc):
        self.wait.until(EC.visibility_of_all_elements_located(loc))
        element = self.get_elements(loc)[-1]
        actions = TouchAction(self.driver)
        if element.is_enabled():
            actions.long_press(x=300, y=(element.location["y"])).move_to(x=300, y=603).release().perform()
        else:
            actions.long_press(x=300, y=2600).move_to(x=300, y=2400).release().perform()

    def hide_keyboard(self):
        self.driver.hide_keyboard()
