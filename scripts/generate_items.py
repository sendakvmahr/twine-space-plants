import csv
import json

result = {}

with open("items.csv") as csvfile:
	reader = csv.reader(csvfile)
	header = next(reader, None)
	for r in reader:
		expiration_info = []
		if r[header.index("expiration_spawn")] != "":
			expiration_spawns = eval(
				r[header.index("expiration_spawn")].replace("“", '"').replace("”", '"')
			)
			expiration_spawn_weights = eval(r[header.index("expiration_spawn_weights")])
			for i in range(len(expiration_spawns)):
				if type(expiration_spawns[i]) is list:
					pool = {}
					for y in range(len(expiration_spawns[i])):
						pool[expiration_spawns[i][y]] = expiration_spawn_weights[i][y]
					expiration_info.append(pool)
				else:
					expiration_info.append({
						expiration_spawns[i]: expiration_spawn_weights[i]
						})
		result[r[header.index("item_name")]] = {
			"name": r[header.index("item_name")], 
			"display_name": r[header.index("display_name")],
			"fragility": r[header.index("fragility")],
			"lifespan": r[header.index("lifespan")],
			"raw_value": r[header.index("raw_value")],
			"dimensions": [r[header.index("dimension_x")], r[header.index("dimension_y")]],
			"expiration_function": r[header.index("expiration_function")],
			"on_expiration": expiration_info,
			"description": r[header.index("description")],
		}
print("<<set setup.items = " + json.dumps(result, indent=4) + ">>")
