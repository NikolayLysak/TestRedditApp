from appium.webdriver.common.appiumby import AppiumBy

from src.pages.base_page import Base


class SearchPage(Base):
    search_button = (
        AppiumBy.XPATH, "//*[@resource-id='com.reddit.frontpage:id/search_view' or @content-desc='Search']"
    )
    search_field = (AppiumBy.ID, "com.reddit.frontpage:id/search")
    search_results = (AppiumBy.ID, "com.reddit.frontpage:id/community_name")

    def start_search_by_keyword(self, request: str):
        self.get_clickable_element(self.search_button).click()
        self.fill_element_field(self.search_field, request)
        return self

    def selecting_a_search_criterion(self, request: str):
        results = self.get_all_visible_elements(self.search_results)
        for result in results:
            if (result.get_attribute("text") == f'r/{request}') | (result.get_attribute("text") == f'{request}'):
                result.click()
                break
            elif results.index(result) == len(results) - 1:
                raise Exception("There are no results satisfying the specified sorting criterion.")
