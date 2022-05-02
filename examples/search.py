from thingiverse import ThingiverseClient
from os.path import dirname
from pprint import pprint
import json

with open(dirname(__file__)+"/../config.json", "rt") as f:
    data = json.loads(f.read())

client = ThingiverseClient(app_token=data["app_token"], debug=True)

res = client.search_things("covid")
pprint(res["hits"][0])