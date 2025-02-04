## REST APIs of the Benchmark

### Content

This folder contains all REST APIs of the benchmark. Each API has a folder, containing :

- An OpenAPI Specification, in the JSON format.
- A Postman Collection, in the JSON format (not always available).
- A README document, containing information regarding the REST API.

### Additional Information

- When trying to open the OpenAPI Specifications in Python (`with open(api, "r") as file:`), do not forget to add the parameter `encoding="utf-8-sig"`. This increases the reliability of UTF-8 encoding detection, as some specifications can contain specific characters.