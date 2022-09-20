from typing import List

from pydantic.main import BaseModel


class Post(BaseModel):
    title: str
    name: str
    posted: str
    comments: str
    vote: str


class Helper:

    # Parse string to list of Objects:
    @staticmethod
    def parse_to_list_of_objects(row_data: list) -> List[Post]:
        response = list(map(lambda obj: Post(**obj), row_data))
        return response

    # Sort data by vote value
    @staticmethod
    def sort_entries_by_accessibility(collection: List[Post], descending=True) -> List[Post]:
        collection.sort(key=lambda obj: int(obj.vote), reverse=descending)
        return collection

    # Filter response data by empty Vote volume
    @staticmethod
    def filter_entries_by_votes(collection: List[Post]) -> List[Post]:
        filtered_resp = list(filter(lambda obj: obj.vote != "Vote", collection))
        assert len(filtered_resp) > 0, "The list is empty, not a single item that meets the filtering criteria"
        return filtered_resp

    @staticmethod
    def select_result(collection: list) -> List[Post]:
        result_collection = Helper.sort_entries_by_accessibility(
            Helper.filter_entries_by_votes(
                Helper.parse_to_list_of_objects(collection)
            )
        )
        return result_collection

    @staticmethod
    def output_of_results(collection: List[Post]):
        max_vote_value = collection[0].vote
        results = list(filter(lambda obj: obj.vote == max_vote_value, collection))
        for result in results:
            print(f'\n\nTopic title: "{result.title}"'
                  f'\nAuthor: {result.name.split("/")[1]}'
                  f'\nDate of posting: {result.posted.strip().split(" ")[1]}'
                  f'\nCommentaries: {result.comments}')
