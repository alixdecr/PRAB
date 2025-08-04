import json


"""
Function used to filter REST APIs from the benchmark.
"""
def filter_apis(filter_data):

    with open("structural-characteristics/structural-characteristics.json", "r") as file:
        api_dict = json.load(file)

    selected_apis = []

    for api_data in api_dict.values():

        canAdd = True

        for filter in filter_data:
            if api_data[filter] != filter_data[filter] and api_data[filter] != "both":
                canAdd = False

        if canAdd:
            selected_apis.append(api_data["id"])
            
    return selected_apis


# THIS IS A TEST TO DEMONSTRATE HOW THE FILTERING FUNCTION WORKS
print(filter_apis({
    "availability": "online",
    "authentication": "no"
}))