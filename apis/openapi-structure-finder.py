import json

with open("apis/features-service/features-service-openapi.json", "r", encoding="utf-8-sig") as openfile:
    dic = json.load(openfile)

structureDict = {
    "routes": {
        "list": [],
        "total": 0,
        "http-methods": {}
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
        if method not in structureDict:
            structureDict[method] = {"list": [], "total": 0}
        structureDict[method]["list"].append(route)
        structureDict[method]["total"] += 1
        if "parameters" in dic["paths"][route][method]:
            for param in dic["paths"][route][method]["parameters"]:
                if "name" in param and "in" in param:
                    if param["name"] not in structureDict["parameters"]["list"] and param["in"] == "query":
                        structureDict["parameters"]["list"].append(param["name"])
                        structureDict["parameters"]["total"] += 1

print(json.dumps(structureDict, indent=4))