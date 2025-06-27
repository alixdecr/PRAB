import json


def filter_apis(filter_data):

    with open("./structural-characteristics/structural-characteristics.json", "r") as openfile:
        api_dict = json.load(openfile)

    selected_apis = []

    for api_data in api_dict.values():
        if all(api_data.get(key) == value for key, value in filter_data.items()):
            selected_apis.append(api_data["id"])
            
    return selected_apis


# THIS IS A TEST TO DEMONSTRATE HOW THE FILTERING FUNCTION WORKS
print(filter_apis({
    "availability": "online",
    "authentication": "no"
}))