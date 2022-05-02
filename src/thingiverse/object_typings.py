from typing import TypedDict, List, Union
from datetime import date


class Maker(TypedDict):
    """
    A maker (user) in Thingiverse.
    """

    accept_tips: bool
    """Is the maker accepting tips?"""
    count_of_designs: int
    """The number of designs the maker has made."""
    count_of_followers: int
    """The number of followers."""
    count_of_following: int
    """The number of makers the maker is following."""
    cover: str
    """"""
    first_name: str
    """"""
    id: int
    """"""
    last_name: str
    """"""
    location: str
    """"""
    name: str
    """"""
    public_url: str
    """"""
    thumbnail: str
    """"""
    url: str


class Tag(TypedDict):
    """
    A tag in Thingiverse.
    """

    absolute_url: str
    """"""
    count: int
    """"""
    name: str
    """"""
    tag: str
    """"""
    things_url: str
    """"""
    url: str


class Thing(TypedDict):
    """
    A thing in Thingiverse.
    """

    comment_count: int
    """When was it uploaded."""
    created_at: date
    """Who made it."""
    creator: Maker
    """"""
    id: str
    """"""
    is_nsfw: Union[bool, None]
    """"""
    is_private: Union[bool, None]
    """"""
    is_published: Union[bool, None]
    """"""
    is_purchased: Union[bool, None]
    """"""
    like_count: int
    """"""
    make_count: int
    """"""
    name: str
    """"""
    preview_image: str
    """"""
    public_url: str
    """"""
    tags: List[Tag]
    """"""
    thumbnail: str
    """"""
    url: str
