from typing import Dict
from requests import get
from datetime import datetime
from .response_typings import ThingsResponse
from .query_typings import SearchThingsQuery


class ThingiverseClient:

    __url: str = "https://api.thingiverse.com"
    __debug: bool = False
    app_token: str = ""

    def __init__(self, app_token: str = "", debug: bool = False):
        self.__debug = debug
        self.app_token = app_token
        return

    def __convert_date(self, v):
        return datetime.strptime(v, "%Y-%m-%dT%H:%M:%S%z")

    def __convert_json(self, d: Dict):
        """
        Converts json keys to underscore case and converts dates into date time objects.
        """
        for k, v in d.items():
            if isinstance(v, dict):
                self.__convert_json(v)
            elif isinstance(v, list):
                for obj in v:
                    if isinstance(obj, dict):
                        self.__convert_json(obj)
            elif k in ["created_at"]:
                d[k] = self.__convert_date(v)
        return d

    def __get(self, path: str, params: Dict = {}) -> Dict:

        url = self.__url + path + "?access_token=" + self.app_token

        if self.__debug:
            print("|- Query:", url)
            print("|- Params:", params)

        r = get(url, params=params, timeout=5)

        if r.ok:
            return self.__convert_json(r.json())
        else:
            print("|- ", r.status_code)
            raise Exception("|- Error with request")

    def hello(self) -> str:
        return "world"

    def search_things(
        self, term: str, params: SearchThingsQuery = {}
    ) -> ThingsResponse:
        return self.__get("/search/" + term, params)
