import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.config_reader import ConfigReader
from src.pages.login_page import LoginPage
from src.pages.results_page import ResultsPage
from src.pages.search_page import SearchPage
from src.utils.helper import Helper


@pytest.fixture
def get_driver():
    desired_caps = ConfigReader().get_desired_caps()
    executor = ConfigReader().get_url()
    driver = webdriver.Remote(command_executor=executor,
                              options=UiAutomator2Options().load_capabilities(desired_caps), )
    driver.implicitly_wait(5)
    print("\nSetUp mobile driver")
    yield driver
    driver.quit()
    print("\nTear down mobile driver")


def test_skip_registration(get_driver):
    login_page = LoginPage(get_driver)
    search_page = SearchPage(get_driver)
    results_page = ResultsPage(get_driver)

    login_page.click_skip()
    search_page.search_info("Banking").select_search_result("Banking")
    collection = results_page.sort_results().collect_results()
    result = Helper().select_result(collection)
    Helper.output_of_results(result)

