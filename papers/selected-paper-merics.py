import json

data = {
        "keywords": {},
        "published": {},
        "authors": {}
        }

with open("papers/selected-papers.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        
        if line:
            elements = line.lower().split(" | ")

            published = elements[3]
            keywords = elements[2].split(", ")
            authors = elements[1].split(", ")

            if published not in data["published"]:
                data["published"][published] = 0

            data["published"][published] += 1

            for k in keywords:
                if k not in data["keywords"]:
                    data["keywords"][k] = 0

                data["keywords"][k] += 1

            for a in authors:
                if a not in data["authors"]:
                    data["authors"][a] = 0

                data["authors"][a] += 1



print(json.dumps(data, indent=4))