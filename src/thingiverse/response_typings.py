from typing import TypedDict, List
from .object_typings import Thing


class Response(TypedDict):
    total: int


class ThingsResponse(Response):
    hits: List[Thing]
