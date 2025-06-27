import json


def filter_apis(filter_data):

    selected_apis = []
    api_dict = {}

    with open("./structural-characteristics/structural-characteristics.json", "r") as openfile:
        api_dict = json.load(openfile)

    for api in api_dict:
        api_data = api_dict[api]

        canAdd = True

        for filter in filter_data:
            if api_data[filter] != filter_data[filter]:
                canAdd = False

        if canAdd:
            selected_apis.append(api_data["id"])
            
    return selected_apis


print(filter_apis({
    "availability": "online",
    "authentication": "no"
}))