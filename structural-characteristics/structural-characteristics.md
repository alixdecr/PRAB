### Structural Characteristics of the REST APIs from the Benchmark

This folder contains the structural characteristics of the REST APIs from the benchmark (in the structural-characteristics.pdf file).

Below, you can find additional information regarding the structural characteristics found in the file :

- `API Name`: The name of the REST API from the benchmark.

- `Reference`: The URL leading to the reference that was used to analyze the structural characteristics of the REST API. This can be the official website of the API, its GitHub repository, a Postman collection, etc.

- `Availability`: The availability of the API:
    - `LOCAL`: The API has to be deployed locally.
    - `ONLINE`: The API is hosted on a web server online.
    - `BOTH`: The API can be used locally or online.

- `Authentication`: The authentication method to access the API:
    - `KEY`: The API requires an access key for user authentication.
    - `NO`: The API does not require any form of authentication.

- `Pricing`: The pricing required to use the API:
    - `YES`: The API has a mandatory pricing plan.
    - `NO`: The API does not have any pricing plan, and is entirely free to use.
    - `OPT`: The API has an optional pricing plan, yet can still be used freely.

- `Limits`: The request rate limits and/or quotas when using the API:
    - `YES`: The API has a rate limit and/or a quota per minute, hour, or day.
    - `NO`: The API does not have a rate limit or a quota.

- `Number of Routes`: The total number of routes contained in the API. As a single route can handle multiple HTTP methods at once (e.g. `/cart` route, with GET to see the cart and POST to add items to it), it is plausible that an API contains less routes than HTTP methods.

- `Number of Query Parameters`: The total number of unique query parameters from all routes contained in the API. For example, if a fictive API contains a `/getPet` route accepting the parameters `[id, name, species]` and a `/getStore` route accepting the parameters `[id, location]`, the set of query parameters for the API consists of `[id, name, species, location]`.

- `GET`: The total number of routes of the GET HTTP method contained in the API.

- `POST`: The total number of routes of the POST HTTP method contained in the API.

- `PUT`: The total number of routes of the PUT HTTP method contained in the API.

- `DELETE`: The total number of routes of the DELETE HTTP method contained in the API.

- `PATCH`: The total number of routes of the PATCH HTTP method contained in the API.

- `OpenAPI URL`: The URL leading to the reference that was used to find/generate the OpenAPI specification.

- `Chart Number`: The number associated with the API name in the research paper.