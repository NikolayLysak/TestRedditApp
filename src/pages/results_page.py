from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import Base


class ResultsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    sort_description_button = ("id", "com.reddit.frontpage:id/sort_description")
    sort_value = (
        "xpath", "//*[@resource-id='com.reddit.frontpage:id/bottomsheet_recycler_view']/android.view.ViewGroup[1]")
    link_list = ("id", "com.reddit.frontpage:id/link_list")
    result_bodies = ("xpath", "//*[@resource-id='com.reddit.frontpage:id/link_left_holder']/..")
    result_titles = ("id", "com.reddit.frontpage:id/title")
    result_votes = ("id", "com.reddit.frontpage:id/vote_view_score")
    result_time_posted = ("id", "com.reddit.frontpage:id/time_posted_label")
    result_users = ("id", "com.reddit.frontpage:id/link_alt_link_label")
    result_comments = ("id", "com.reddit.frontpage:id/comments")

    def sort_results(self):
        self.wait.until(EC.element_to_be_clickable(self.get_element(self.sort_description_button)))
        self.get_element(self.sort_description_button).click()
        self.wait.until(EC.visibility_of(self.get_element(self.sort_value)))
        self.get_element(self.sort_value).click()
        return self

    def collect_results(self):
        list_of_result_entries = list()
        while len(list_of_result_entries) <= 20:
            self.swipe_element(self.result_bodies)
            page_entries = self.get_elements(self.result_bodies)

            for entry in page_entries:
                index = page_entries.index(entry)
                if index < (len(page_entries) - 1):
                    new_obj = {
                        "title": self.get_elements(self.result_titles)[index].get_attribute("text"),
                        "name": self.get_elements(self.result_users)[index].get_attribute("text"),
                        "posted": self.get_elements(self.result_time_posted)[index].get_attribute("text"),
                        "vote": self.get_elements(self.result_votes)[index].get_attribute("text"),
                        "comments": self.get_elements(self.result_comments)[index].get_attribute("text")
                    }
                    list_of_result_entries.append(new_obj)
        return list_of_result_entries
