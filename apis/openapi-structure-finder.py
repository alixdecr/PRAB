import json

with open("apis/quartz-manager/quartz-manager-openapi.json", "r", encoding="utf-8") as openfile:
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

print(f"No. Routes: {structureDict['routes']['total']}")
print(f"No. Query Parameters: {structureDict['parameters']['total']}")
if "get" in structureDict:
    print(f"No. GET: {structureDict['get']['total']}")
if "post" in structureDict:
    print(f"No. POST: {structureDict['post']['total']}")
if "put" in structureDict:
    print(f"No. PUT: {structureDict['put']['total']}")
if "delete" in structureDict:
    print(f"No. DELETE: {structureDict['delete']['total']}")
if "patch" in structureDict:
    print(f"No. PATCH: {structureDict['patch']['total']}")