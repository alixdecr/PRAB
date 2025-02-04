# PRAB

Public REST API Benchmark (PRAB). This GitHub repository contains the OpenAPI Specification (OAS) / Postman Collection of over 60 publicly available REST APIs.

## Related Research Paper

PRAB was created in parallel to the research paper *A Public Benchmark of REST APIs (A. Decrop, S. Eraso, X. Devroey, G. Perrouin)*, which was accepted for inclusion in the *22nd International Conference on Mining Software Repositories (MSR 2025)*. **When using our benchmark, please refer to this research paper for citation purposes.**

## Main Goal

The main goal of this repository is to provide a public benchmark of REST APIs, for the evaluation of research related to REST APIs. For instance, a new testing tool can leverage the OpenAPI specifications provided in this repository.

## Main Content

The main content of the benchmark can be found in the `/apis` folder. At the moment, each REST API of the benchmark has its sub-folder, containing an available (and up-to-date) OpenAPI Specification (in the JSON format). Certain APIs also have an available Postman Collection.

## Additional Content

The repository also contains 2 additional folders:

- `/structural-characteristics`: This folder contains various information regarding structural characteristics for each API of the benchmark. More details can be found in the folder.

- `/study-data`: This folder contains the study data associated with the research paper. You can find the following files:
    - `filtered-papers.md`: Contains the research papers that were found with our search string, in our systematic mapping study.
    - `selected-papers.md`: Contains the research papers that were accepted in our systematic mapping study.
    - `study-apis.md`: Contains the REST APIs that were found in the research papers (from `selected-papers.md`).
 
## Actionable Insights and Guidance on Using the Benchmark

The main outcome of this research is our benchmark backed by a systematic mapping study. Our goal was not to evaluate the design quality of REST APIs but to provide an unbiased and comprehensive benchmark containing documentation and structural characteristics of 60 public REST APIs. The benchmark is aimed to be used by users, testers, and researchers in their evaluations. We cannot assert that a certain API is *better* compared to another API in the benchmark. Indeed, as REST is not a standard but rather an architectural style, there are multiple ways to implement a REST API. Indeed, the structure of a REST API can drastically change from one API to another API. For instance, an API could contain a single GET route with various usable query parameters (e.g., a `/users` route with the query parameters `id`, `name`, `age`). On the other hand, an API could contain a lot of different specialized GET routes without any query parameters (e.g., the routes `/user/{id}`, `/user/{name}`, `/user/{age}`).

Moreover, REST APIs utilize different HTTP methods depending on their application domain. For instance, APIs specialized in retrieving data (e.g., a weather API to retrieve the current weather, precipitation index, or weekly forecast) would contain various routes with the GET HTTP method. Other APIs specialized in sending data (e.g., a booking API to book a hotel room, order food, or send a payment) would contain various routes with the POST HTTP method. Similarly, update-heavy APIs would utilize the PATCH (modify parts of a resource) and PUT (create or replace a resource) HTTP methods.

Therefore, we leave the selection of APIs up to the benchmark users but provide concrete metrics to support evidence-based API selection. For instance, a tool for REST API security testing might require the evaluation of APIs that allow data to be sent to the server (i.e., with the POST HTTP method). The evaluation of such a tool would utilize a subset of our benchmark, comprising APIs with a high distribution of POST methods. In consequence, the structural characteristics provided in our benchmark enable researchers to filter the APIs they find relevant (i.e., that match specific experimental needs), without the necessity to utilize all 60 APIs.

For research implying source code analysis, we include URLs for downloading (local) or using (online) the REST APIs. Our quality criteria excluded non-deployable APIs. Fuzzing research also cares about request rate limits, pricing, and authentication mechanisms, which we also include. Finally, we provide up-to-date documentation in both OpenAPI/Postman formats, which testing tools can leverage. We did not include API source code in our benchmark but rather reference it via respective URLs (GitHub repositories, website downloads, etc.).
