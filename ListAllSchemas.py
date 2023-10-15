
from google.cloud import contentwarehouse
import os

def sample_list_document_schemas(project_number: str, location: str) -> None:
    document_schema_client = contentwarehouse.DocumentSchemaServiceClient()
    parent = document_schema_client.common_location_path(
        project=project_number, location=location
    )
    print(parent)
    # Initialize request argument(s)
    request = contentwarehouse.ListDocumentSchemasRequest(
        parent=parent,
    )

    # Make the request
    page_result = document_schema_client.list_document_schemas(request=request)

    # Print response
    responses = []
    for response in page_result:
        print(response)
        responses.append(response)

    return responses

