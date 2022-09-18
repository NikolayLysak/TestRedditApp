from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import Base


class SearchPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    search_button = ("accessibility_id", "Search")
    search_field = ("id", "com.reddit.frontpage:id/search")
    search_results = ("id", "com.reddit.frontpage:id/community_name")

    def start_search_by_keyword(self, request: str):
        self.wait.until(EC.element_to_be_clickable(self.get_element(self.search_button)))
        self.get_element(self.search_button).click()
        self.get_element(self.search_field).send_keys(request)
        return self

    def selecting_a_search_criterion(self, request: str):
        results = self.get_elements(self.search_results)
        for result in results:
            if result.get_attribute("text") == f'r/{request}':
                result.click()
                break
