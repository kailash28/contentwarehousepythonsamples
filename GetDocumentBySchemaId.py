
from google.cloud import contentwarehouse


def get_document_schema_by_id(
    project_number: str, location: str, document_schema_id: str
) -> None:
  
    document_schema_client = contentwarehouse.DocumentSchemaServiceClient()
    document_schema_path = document_schema_client.document_schema_path(
        project=project_number,
        location=location,
        document_schema=document_schema_id,
    )

    # Initialize request argument(s)
    request = contentwarehouse.GetDocumentSchemaRequest(
        name=document_schema_path,
    )

    # Make the request
    response = document_schema_client.get_document_schema(request=request)

    # Handle the response
    print("Document Schema:", response)

    return response
