from datetime import datetime
import json, requests


"""
Function used to update REST APIs of the benchmark.
"""
def update_apis():

    date = datetime.now().strftime("%Y-%m-%d")

    with open("structural-characteristics/structural-characteristics.json", "r") as file:
        api_dict = json.load(file)

    for api_id, data in api_dict.items():

        print(f"Updating {api_id}...")

        oas_data = get_oas_data(api_id)
        is_local = data["characteristics"]["availability"] == "local"

        oas_badge = generate_oas_badge(oas_data)
        server_badge = generate_server_badge(oas_data, is_local)

        badges = f"{oas_badge} {server_badge}\n\n"
        last_check = f"Last Checked: {date}\n\n"
        markdown_readme = generate_markdown_readme(api_id, data)

        content = badges + last_check + markdown_readme

        with open(f"apis/{api_id}/README.md", "w") as file:
            file.write(content)

        print(f"Finished updating {api_id}.")


"""
Function used to generate a markdown readme string for a REST API of the benchmark.
"""
def generate_markdown_readme(api_id, data):

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

    content += f"- Identifier: {api_id}\n\n"
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


"""
Function which generates a markdown string for the OAS badge of a benchmark REST API.
"""
def generate_oas_badge(oas_data):

    badge = "![alt text](https://img.shields.io/badge/OpenAPI_Specification-"

    if oas_data == {}:
        badge += "Invalid-red"
    elif "openapi" not in oas_data:
        badge += "Oudated-orange"
    else:
        badge += "Valid-brightgreen"

    badge += ".svg)"

    return badge


"""
Function which generates a markdown string for the server badge of a benchmark REST API.
"""
def generate_server_badge(oas_data, is_local):

    badge = "![alt text](https://img.shields.io/badge/Server_URL-"

    server_url = get_server_url(oas_data)

    if server_url is None:
        badge += "Missing-orange"
    elif is_local:
        badge += "Local-green"
    elif not is_valid_server_url(server_url):
        badge += "Invalid-red"
    else:
        badge += "Valid-brightgreen"

    badge += ".svg)"

    return badge


"""
Function used to get OAS file data for a REST API of the benchmark.
"""
def get_oas_data(api_id):

    oas_path = f"apis/{api_id}/{api_id}-openapi.json"

    try:
        with open(oas_path, "r", encoding="utf-8-sig") as file:
            oas_data = json.load(file)

        return oas_data

    except:
        return {}
    

"""
Function used to get the server URL from OAS data for a REST API of the benchmark.
"""
def get_server_url(oas_data):

    try:
        server_url = oas_data["servers"][0]["url"]
        return server_url
    
    except:
        return None


"""
Function used to check if a server URL is still valid for a REST API of the benchmark.
"""
def is_valid_server_url(server_url):

    try:
        response = requests.get(server_url, timeout=10)
        return True
    
    except:
        return False

    
update_apis()