from google.cloud import contentwarehouse



def sample_delete_document_schema(
    project_number: str, location: str, document_schema_id: str
) -> None:
    # Create a client
    document_schema_client = contentwarehouse.DocumentSchemaServiceClient()

    # The full resource name of the location, e.g.:
    # projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}
    document_schema_path = document_schema_client.document_schema_path(
        project=project_number,
        location=location,
        document_schema=document_schema_id,
    )

    # Initialize request argument(s)
    request = contentwarehouse.DeleteDocumentSchemaRequest(
        name=document_schema_path,
    )

    # Make the request
    response = document_schema_client.delete_document_schema(request=request)

    return response


