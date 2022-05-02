from typing import TypedDict, List
from enum import Enum


class SortMethod(Enum):
    """
    Sort methods.
    """

    RELEVANT = "relevant"
    TEXT = "text"
    POPULAR = "popular"
    MAKES = "makes"
    NEWEST = "newest"


class PaginatedQuery(TypedDict, total=False):
    """
    Paginated query params.
    """

    page: int
    """The page to return."""
    per_page: int
    """How many results per page."""


class SearchThingsQuery(PaginatedQuery, total=False):
    """
    Search query params. Extends PaginatedQuery params. A query can feature all or non of these elements.
    """

    sort: SortMethod
    """"""
    posted_before: str
    """"""
    posted_after: str
    """"""
    is_edu_approved: bool
    """"""
    subjects: List[str]
    """"""
    grades: List[str]
    """"""
    standards: List[str]
    """"""
    license: str
    """"""
    customizable: bool
    """"""
    show_customized: bool
    """"""
    order_print: bool
    """"""
    has_makes: bool
    """"""
    is_featured: bool
    """"""
    is_challenge_winner: bool
    """"""
    liked_by: str
    """"""
    collected_by: str
    """"""
    made_by: str
    """"""
    is_derivative: bool
    """"""
    category_id: str
