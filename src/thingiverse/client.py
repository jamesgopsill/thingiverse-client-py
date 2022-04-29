from typing import Dict
from requests import get

class ThingiverseClient:

    __url: str = "https://api.thingiverse.com"
    __debug: bool = False
    __app_token: str = ""

    def __init__(self, app_token: str, debug: bool = False):
        self.__debug = debug
        self.__app_token = app_token
        return

    def hello(self) -> str:
        return "world"

    def __get(self, path: str, params: Dict = {}) -> Dict:

        url = self.__url + path + "?access_token=" + self.__app_token

        if self.__debug:
            print("|- Query:", url)
            print("|- Params:", params)

        r = get(url, params=params, timeout=5)
        
        if r.ok:
            return self.__convert_json(r.json())
        else:
            print("|- ", r.status_code)
            raise Exception("|- Error with request")

    def search(self, term: str) -> Dict:
        return self.__get("/search/" + term)