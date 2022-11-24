import json 

with open("data/last_activity_2022-08-13.json", "r") as file:
    data = json.load(file)

# print(data)

def process_activities(d=data):
    data_nor_list_dicts = {k: val for (k, val) in data.items() if not isinstance(
        val, list) | isinstance(val, dict)}
    return {k: val for (k, val) in data_nor_list_dicts.items() if val != None}

data = process_activities()
print(data)