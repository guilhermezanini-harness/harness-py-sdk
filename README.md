## Prerequisites

Before running the script, ensure that you have installed the required libraries. You can install them via pip using the following commands:

```bash
pip install requests pyyaml
```

- `requests`: This library is required for making HTTP requests to the Harness platform.
- `pyyaml`: This library is necessary for handling YAML files. It may be required by the script for configuration or data manipulation.

## Getting Started

The first step to utilize this SDK is to authenticate with Harness API, you achieve the following by doing the below:

```python
harness_service = HarnessBaseService(os.environ.get('HARNESS_PLATFORM_API_KEY'), "my-account-identifier")
```

### Example 1 - Listing Services

```python
harness_service.services.fetch_services()
```

### Example 2 - Listing Connectors using the old API

```python
harness_service.connectors.old.fetch_connectors_listV2(
    data={
        "types": ["HttpHelmRepo"],
        "filterType": "Connector"
    },
    org_identifier=org_identifier,
    project_identifier=project_identifier
)
```

## Reference

| Class          | Documentation URL                                                                                       |
|----------------|----------------------------------------------------------------------------------------------------------|
| Connectors     | [Link](https://guilhermezanini-harness.github.io/harness-py-sdk/harness_py_sdk/harness_connectors.html)                   |
| Old Connectors | [Link](https://guilhermezanini-harness.github.io/harness-py-sdk/harness_py_sdk/harness_old_connectors.html)               |
| Pipelines      | [Link](https://guilhermezanini-harness.github.io/harness-py-sdk/harness_py_sdk/harness_pipelines.html)                     |
| Services       | [Link](https://guilhermezanini-harness.github.io/harness-py-sdk/harness_py_sdk/harness_services.html)                     |
| Templates      | [Link](https://guilhermezanini-harness.github.io/harness-py-sdk/harness_py_sdk/harness_templates.html)                     |