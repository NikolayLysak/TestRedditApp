from appium.webdriver.common.appiumby import AppiumBy

from src.pages.base_page import Base


class ResultsPage(Base):
    sort_description_button = (AppiumBy.ID, "com.reddit.frontpage:id/sort_description")
    link_list = (AppiumBy.ID, "com.reddit.frontpage:id/link_list")
    result_bodies = (
        AppiumBy.XPATH, "//*[@resource-id='com.reddit.frontpage:id/link_left_holder']/../android.widget.LinearLayout"
    )
    result_titles = (AppiumBy.ID, "com.reddit.frontpage:id/title")
    result_votes = (AppiumBy.ID, "com.reddit.frontpage:id/vote_view_score")
    result_time_posted = (AppiumBy.ID, "com.reddit.frontpage:id/time_posted_label")
    result_users = (AppiumBy.ID, "com.reddit.frontpage:id/link_alt_link_label")
    result_comments = (AppiumBy.ID, "com.reddit.frontpage:id/comments")

    @staticmethod
    def sort_by_locator(sort_by_criterion: str) -> tuple:
        return AppiumBy.XPATH, f'//*[contains(@text, "{sort_by_criterion}")]/..'

    def selecting_the_sorting_of_results(self, sort_by_criterion: str):
        self.get_clickable_element(self.sort_description_button).click()
        self.get_visible_element(self.sort_by_locator(sort_by_criterion)).click()
        return self

    def collect_results(self) -> list[dict]:
        list_of_result_entries = list()
        iteration = 0

        while len(list_of_result_entries) <= 20:
            iteration += 1
            saved_len = len(list_of_result_entries)
            self.scroll_results_list(self.result_bodies)

            page_entries = self.get_all_visible_elements(self.result_bodies)
            for entry in page_entries:
                index = page_entries.index(entry)
                if index < (len(page_entries) - 1):

                    # Creating a new object from the post data on the page
                    new_obj = {
                        "title": self.get_all_visible_elements(self.result_titles)[index].get_attribute("text"),
                        "name": self.get_all_visible_elements(self.result_users)[index].get_attribute("text"),
                        "posted": self.get_all_visible_elements(self.result_time_posted)[index].get_attribute("text"),
                        "vote": self.get_all_visible_elements(self.result_votes)[index].get_attribute("text"),
                        "comments": self.get_all_visible_elements(self.result_comments)[index].get_attribute("text")
                    }
                    list_of_result_entries.append(new_obj)

                    # Emergency exit in case of infinite cycle
                    if iteration == 3:
                        assert saved_len < len(list_of_result_entries), \
                            "The list of posts is not filled with data. Perhaps there are no search results for " \
                            "this query or their number is less than the required condition"

        return list_of_result_entries
