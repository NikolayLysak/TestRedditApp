import allure
import pytest
from appium import webdriver

from config.config_reader import ConfigReader
from src.pages.login_page import LoginPage
from src.pages.results_page import ResultsPage
from src.pages.search_page import SearchPage
from src.utils.helper import Helper


@pytest.fixture(scope="session")
def get_driver():
    with allure.step("Starting the 'Reddit' application"):
        print("\nSetUp mobile driver")
        driver = webdriver.Remote(
            command_executor=ConfigReader().get_url(),
            desired_capabilities=ConfigReader().get_desired_caps()
        )
        yield driver
        print("\nTear down mobile driver")
        driver.quit()


@allure.parent_suite("Mobile")
@allure.suite("Reddit App sort")
@allure.title("Selecting the result with the most Up Votes.")
def test_skip_registration(get_driver):
    login_page = LoginPage(get_driver)
    search_page = SearchPage(get_driver)
    results_page = ResultsPage(get_driver)

    with allure.step("Skip logging in the app"):
        login_page.skip_registration()

    with allure.step("Search for posts on Banking"):
        search_page.start_search_by_keyword("Banking").selecting_a_search_criterion("Banking")

    with allure.step("Selecting 20+ hottest posts from the list of results"):
        collection = results_page.selecting_the_sorting_of_results("Hot").collect_results()

    with allure.step("Selecting a post from the list with the maximum number of up votes"):
        Helper.output_of_results(
            Helper.select_result(collection)
        )
