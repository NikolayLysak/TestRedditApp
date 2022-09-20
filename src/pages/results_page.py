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

    def collect_results(self, min_items_count_to_collect=20) -> list[dict]:
        list_of_result_entries = list()
        saved_list_of_results = list()
        iteration = 0

        while len(list_of_result_entries) <= min_items_count_to_collect:
            iteration += 1
            self.scroll_results_list(self.result_bodies)
            titles_list = self.get_all_visible_elements(self.result_titles)
            names_list = self.get_all_visible_elements(self.result_users)
            posted_list = self.get_all_visible_elements(self.result_time_posted)
            votes_list = self.get_all_visible_elements(self.result_votes)
            comments_list = self.get_all_visible_elements(self.result_comments)

            for index, entry in enumerate(self.get_all_visible_elements(self.result_bodies)[:-1]):
                saved_list_of_results.extend(list_of_result_entries)

                # Creating a new object from the post data on the page
                list_of_result_entries.append({
                    "title": titles_list[index].text,
                    "name": names_list[index].text,
                    "posted": posted_list[index].text,
                    "vote": votes_list[index].text,
                    "comments": comments_list[index].text
                })

            # Emergency exit in case of infinite cycle
            if iteration == 3:
                assert saved_list_of_results[-1].get("title") != list_of_result_entries[-1].get("title"), \
                    "The list of posts is not filled with data. Perhaps there are no search results for " \
                    "this query or their number is less than the required condition"

        return list_of_result_entries
