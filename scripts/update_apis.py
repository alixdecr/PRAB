import json


"""
Function used to update REST APIs of the benchmark.
"""
def update_apis():

    with open("structural-characteristics/structural-characteristics.json", "r") as openfile:
        api_dict = json.load(openfile)

    for id, data in api_dict.items():
        markdown_readme = generate_markdown_readme(id, data)

        with open(f"apis/{id}/README.md", "w") as file:
            file.write(markdown_readme)

"""
Function used to generate a markdown readme string for a REST API of the benchmark.
"""
def generate_markdown_readme(id, data):

    name = data["name"]
    used_by = data["used-by"]
    website_reference = data["references"]["website"]
    openapi_reference = data["references"]["openapi"]

    availability = data["characteristics"]["availability"].capitalize()
    authentication = data["characteristics"]["authentication"].capitalize()
    pricing = data["characteristics"]["pricing"].capitalize()
    request_limits = data["characteristics"]["request-limits"].capitalize()

    routes = data["characteristics"]["routes"]
    query_parameters = data["characteristics"]["query-parameters"]

    http_methods = data["characteristics"]["http-methods"]
    total_http_methods = sum(http_methods.values())

    content = f"## {name} API: Structural Characteristics\n\n"

    content += "### General Information\n\n"

    content += f"- Identifier: {id}\n\n"
    content += f"- Name: {name}\n\n"
    content += f"- Used By: {used_by} (the citation references can be found in `/study-data/study-apis.md`)\n\n"
    content += f"- References: [API Website]({website_reference}), [OpenAPI Specification]({openapi_reference})\n\n"

    content += "### Usage Information\n\n"

    content += f"- Availability: {availability}\n\n"
    content += f"- Authentication Method: {authentication}\n\n"
    content += f"- Pricing: {pricing}\n\n"
    content += f"- Request Limits: {request_limits}\n\n"

    content += "### Routes and Query Parameters Information\n\n"

    content += f"- Number of Routes: {routes}\n\n"
    content += f"- Number of Query Parameters: {query_parameters}\n\n"

    content += "### HTTP Method Information\n\n"

    content += "| Method | Amount | Percentage |\n"
    content += "|--------|--------|------------|\n"

    for method, count in http_methods.items():
        percent = (count / total_http_methods * 100) if total_http_methods > 0 else 0
        content += f"| `{method.upper()}` | {count} | {percent:.2f}% |\n"

    return content


update_apis()