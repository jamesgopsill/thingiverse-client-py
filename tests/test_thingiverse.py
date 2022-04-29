import unittest
from thingiverse import ThingiverseClient
import json
from os.path import dirname
from pprint import pprint

with open(dirname(__file__)+"/config.json", "rt") as f:
    data = json.loads(f.read())

client = ThingiverseClient(app_token=data["app_token"], debug=True)

class TestThingiverse(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(client.hello(), "world")

    def test_search(self):
        res = client.search("covid")
        pprint(res)
        flag = isinstance(res, dict)
        self.assertEqual(flag, True)
