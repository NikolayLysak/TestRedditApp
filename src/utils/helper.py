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

    # Sort data by accessibility
    @staticmethod
    def sort_entries_by_accessibility(collection: List[Post], descending=True) -> List[Post]:
        collection.sort(key=lambda obj: int(obj.vote), reverse=descending)
        return collection

    # Filter response data by price volume
    @staticmethod
    def filter_entries_by_votes(collection: List[Post]) -> List[Post]:
        filtered_resp = list(filter(lambda obj: (obj.vote != "Vote"), collection))
        assert len(filtered_resp) > 0
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
    def output_of_results(collection: List[Post], index: int = 0) -> None:
        print(f'\n\nTopic title: "{collection[index].title}"')
        print(f'Author: {collection[index].name.split("/")[1]}')
        print(f'Date of posting: {collection[index].posted.strip().split(" ")[1]}')
        print(f'Commentaries: {collection[index].comments}')

        if collection[index].vote == collection[index+1].vote:
            index += 1
            Helper.output_of_results(collection, index)



