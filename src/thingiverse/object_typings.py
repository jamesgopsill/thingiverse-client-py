from typing import TypedDict, List, Union
from datetime import date


class Maker(TypedDict):
    accept_tips: bool
    count_of_designs: int
    count_of_followers: int
    count_of_following: int
    cover: str
    first_name: str
    id: int
    last_name: str
    location: str
    name: str
    public_url: str
    thumbnail: str
    url: str


class Tag(TypedDict):
    absolute_url: str
    count: int
    name: str
    tag: str
    things_url: str
    url: str


class Thing(TypedDict):
    comment_count: int
    created_at: date
    creator: Maker
    id: str
    is_nsfw: Union[bool, None]
    is_private: Union[bool, None]
    is_published: Union[bool, None]
    is_purchased: Union[bool, None]
    like_count: int
    make_count: int
    name: str
    preview_image: str
    public_url: str
    tags: List[Tag]
    thumbnail: str
    url: str
