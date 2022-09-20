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
        for result in self.get_all_visible_elements(self.search_results):
            res_text = result.text
            if res_text in [f'r/{request}', f'{request}']:
                result.click()
                return
        raise Exception("There are no results satisfying the specified sorting criterion.")
