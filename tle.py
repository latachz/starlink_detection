import ephem
from datetime import datetime
import time
import requests as r
from columnar import columnar

all_starlinks_res = r.get(f"https://api.spacexdata.com/v4/starlink")
starlinks = all_starlinks_res.json()

print("All starlinks: ")

starlinks_table = []
headers = ["OBJECT_NAME", "OBJECT_ID", "API_ID"]

for s in starlinks:
	print(starlinks_table.append([s['spaceTrack']['OBJECT_NAME'], s['spaceTrack']['OBJECT_ID'], s['id']]))

print(columnar(starlinks_table, headers, no_borders=True))

starlink_id = input("Starlink id: ")
if starlink_id == "":
	print("You have to give id!")
else:
	starlink_res = r.get(f"https://api.spacexdata.com/v4/starlink/{starlink_id}")
	data = starlink_res.json()

	tle0 = data['spaceTrack']['TLE_LINE0']
	tle1 = data['spaceTrack']['TLE_LINE1']
	tle2 = data['spaceTrack']['TLE_LINE2']

	while True:
		starlink = ephem.readtle(tle0, tle1, tle2)
		starlink.compute(datetime.now())
		print('%s %s' % (starlink.sublong, starlink.sublat))
		time.sleep(1)