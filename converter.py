#!/usr/bin/python

import json

with open("./js/precincts.json") as json_file:
    json_data = json.load(json_file)

with open("./js/precincts-old.json") as json_file:
    old_json_data = json.load(json_file)

old_geoms = {}
for feature in old_json_data['features']:
	old_geoms[feature['properties']['Name']] = feature['geometry']

for feature in json_data['features']:
	feature['geometry'] = old_geoms[feature['properties']['PRECINCT']]

with open("./js/precincts-fixed.json", "w") as outfile:
	json.dump(json_data, outfile)