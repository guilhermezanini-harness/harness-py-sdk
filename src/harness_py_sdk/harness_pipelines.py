class HarnessPipelines:
    def __init__(self, harness_service):
        self.harness_service = harness_service

    def fetch_pipeline_yaml(self, org_identifier, project_identifier, pipeline_identifier):
        endpoint = f"/v1/orgs/{org_identifier}/projects/{project_identifier}/pipelines/{pipeline_identifier}"
        return self.harness_service._make_request("GET", endpoint)
    
    def create_pipeline(self, org_identifier, project_identifier, pipeline_data):
        endpoint = f"/v1/orgs/{org_identifier}/projects/{project_identifier}/pipelines"
        return self.harness_service._make_request("POST", endpoint, json=pipeline_data)
    
    def update_pipeline(self, org_identifier, project_identifier, pipeline_data, pipeline_identifier):
        endpoint = f"/v1/orgs/{org_identifier}/projects/{project_identifier}/pipelines/{pipeline_identifier}"
        return self.harness_service._make_request("PUT", endpoint, json=pipeline_data)
    
    def delete_pipeline(self, org_identifier, project_identifier, pipeline_identifier):
        endpoint = f"/v1/orgs/{org_identifier}/projects/{project_identifier}/pipelines/{pipeline_identifier}"
        return self.harness_service._make_request("DELETE", endpoint)