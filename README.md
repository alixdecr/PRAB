# PRAB

Public REST API Benchmark (PRAB). This GitHub repository contains the OpenAPI Specification (OAS) / Postman collection of over 60 publicly available REST APIs.

## Related Research Paper

PRAB was created in parallel to the research paper *A Public Benchmark of REST APIs* (A. Decrop, S. Eraso, X. Devroey, G. Perrouin), which was accepted for inclusion in the 22nd International Conference on Mining Software Repositories (MSR 2025). **When using our benchmark, please refer to this research paper for citation.**

## Main Goal

The main goal of this repository is to provide a public benchmark of REST APIs, for the evaluation of research related to REST APIs. For instance, a new testing tool can leverage the OpenAPI specifications provided in this repository.

## Main Content

The main content of the benchmark can be found in the `/apis` folder. At the moment, each REST API of the benchmark has its sub-folder, containing an available (and up-to-date) OpenAPI specification / Postman collection (in the JSON format).

## Additional Content

The repository also contains 2 additional folders:

- `/structural-characteristics`: This folder contains various information regarding structural characteristics for each API of the benchmark. More details can be found in the folder.

- `/study-data`: This folder contains the study data associated with the research paper. You can find the following files:
    - `filtered-papers.md`: Contains the research papers that were found with our search string, in our systematic mapping study.
    - `selected-papers.md`: Contains the research papers that were accepted in our systematic mapping study.
    - `study-apis.md`: Contains the REST APIs that were found in the research papers (from `selected-papers.md`).