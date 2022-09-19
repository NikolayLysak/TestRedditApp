from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    driver: WebDriver
    wait: WebDriverWait

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    tool_bar = (AppiumBy.ID, "com.reddit.frontpage:id/toolbar")
    tab_layout = (AppiumBy.ID, "com.reddit.frontpage:id/tab_layout")

    def wait_element_be_disabled(self, locator: tuple):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def get_clickable_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_visible_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_all_visible_elements(self, locator: tuple) -> list[WebElement]:
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def clic_by_element(self, locator: tuple):
        self.get_clickable_element(locator).click()

    def fill_element_field(self, locator: tuple, value: str):
        self.get_visible_element(locator).send_keys(value)

    def get_y_offset(self) -> int:
        offset = self.get_visible_element(self.tool_bar).size['height'] + \
                 self.get_visible_element(self.tab_layout).size['height']
        return offset

    def scroll_results_list(self, locator: tuple):
        elements = self.get_all_visible_elements(locator)

        if elements[-1].is_enabled():
            coord_x1: int = elements[-1].location["x"]
            coord_x2: int = coord_x1
            coord_y1: int = elements[-1].location["y"] - 5
            coord_y2: int = self.get_y_offset()
        else:
            coord_x1: int = 300
            coord_x2: int = 300
            coord_y1: int = 1250
            coord_y2: int = 1000

        actions = ActionChains(self.driver, 2000)
        actions \
            .w3c_actions.pointer_action \
            .move_to_location(coord_x1, coord_y1) \
            .pointer_down() \
            .move_to_location(coord_x2, coord_y2) \
            .release()
        actions.perform()
