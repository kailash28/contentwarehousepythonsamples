
from google.cloud import contentwarehouse


def createSchema(project_number: str, location: str, user_id: str) -> None:
    # Create a Schema Service client
    document_schema_client = contentwarehouse.DocumentSchemaServiceClient()

    # The full resource name of the location, e.g.:
    # projects/{project_number}/locations/{location}
    parent = document_schema_client.common_location_path(
        project=project_number, location=location
    )

    # Define Schema Property of Text Type
    property_definition = contentwarehouse.PropertyDefinition(
        name="stock_symbol",
        display_name="Searchable text",
        is_searchable=True,
        text_type_options=contentwarehouse.TextTypeOptions(),
    )

    # Define Document Schema Request
    create_document_schema_request = contentwarehouse.CreateDocumentSchemaRequest(
        parent=parent,
        document_schema=contentwarehouse.DocumentSchema(
            display_name="My Test Schema",
            property_definitions=[property_definition],
        ),
    )

    # Create a Document schema
    document_schema = document_schema_client.create_document_schema(
        request=create_document_schema_request
    )
    return document_schema
	
