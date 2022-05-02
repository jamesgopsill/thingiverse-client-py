from typing import TypedDict, List
from .object_typings import Thing


class Response(TypedDict):
    """
    A base response class.
    """

    total: int


class ThingsResponse(Response):
    """
    A things response. Extends Response.
    """

    hits: List[Thing]
