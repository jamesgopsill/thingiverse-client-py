from typing import TypedDict, List
from enum import Enum


class SortMethod(Enum):
    RELEVANT = "relevant"
    TEXT = "text"
    POPULAR = "popular"
    MAKES = "makes"
    NEWEST = "newest"


class PaginatedQuery(TypedDict, total=False):
    page: int
    per_page: int


class SearchThingsQuery(PaginatedQuery, total=False):
    sort: SortMethod
    posted_before: str
    posted_after: str
    is_edu_approved: bool
    subjects: List[str]
    grades: List[str]
    standards: List[str]
    license: str
    customizable: bool
    show_customized: bool
    order_print: bool
    has_makes: bool
    is_featured: bool
    is_challenge_winner: bool
    liked_by: str
    collected_by: str
    made_by: str
    is_derivative: bool
    category_id: str
