data = {"papers": 0,
        "accepted": 0,
        "rejected": 0,
        "reject-reason": {},
        "accepted-papers": []}

with open("study-papers/filtered-papers.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        
        if line:
            elements = line.replace(" ", "").lower().split("|")

            if len(elements) > 1:

                data["papers"] += 1

                data[elements[1]] += 1

                if elements[1] == "rejected":
                    if elements[2] not in data["reject-reason"]:
                        data["reject-reason"][elements[2]] = 0

                    data["reject-reason"][elements[2]] += 1

                elif elements[1] == "accepted":
                    data["accepted-papers"].append(elements[0])

print(data)