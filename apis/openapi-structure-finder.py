import json

with open("apis/spotify/spotify-openapi.json", "r", encoding="utf-8") as openfile:
    dic = json.load(openfile)

structureDict = {
    "routes": {
        "list": [],
        "total": 0,
        "http-methods": {}
    },
    "get": {
        "list": [],
        "total": 0
    },
    "post": {
        "list": [],
        "total": 0
    },
    "patch": {
        "list": [],
        "total": 0
    },
    "put": {
        "list": [],
        "total": 0
    },
    "delete": {
        "list": [],
        "total": 0
    },
    "parameters": {
        "list": [],
        "total": 0
    }
}

structureDict["routes"]["list"] = list(dic["paths"].keys())
structureDict["routes"]["total"] = len(structureDict["routes"]["list"])

for route in structureDict["routes"]["list"]:
    structureDict["routes"]["http-methods"][route] = []

    for method in dic["paths"][route]:
        structureDict["routes"]["http-methods"][route].append(method)
        structureDict[method]["list"].append(route)
        structureDict[method]["total"] += 1
        if "parameters" in dic["paths"][route][method]:
            for param in dic["paths"][route][method]["parameters"]:
                if param["name"] not in structureDict["parameters"]["list"]:
                    structureDict["parameters"]["list"].append(param["name"])
                    structureDict["parameters"]["total"] += 1

print(json.dumps(structureDict, indent=4))