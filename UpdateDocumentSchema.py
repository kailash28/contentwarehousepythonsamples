
from google.cloud import contentwarehouse



def update_document_schema(
    project_number: str, location: str, document_schema_id: str
) -> None:
    # Create a Schema Service client
    document_schema_client = contentwarehouse.DocumentSchemaServiceClient()

    # The full resource name of the location, e.g.:
    # projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}
    document_schema_path = document_schema_client.document_schema_path(
        project=project_number,
        location=location,
        document_schema=document_schema_id,
    )

    # Define Schema Property of Text Type with updated values
    updated_property_definition = contentwarehouse.PropertyDefinition(
        name="stock_symbol",  # Must be unique within a document schema (case insensitive)
        display_name="Searchable text",
        is_searchable=True,
        is_repeatable=False,
        is_required=True,
        text_type_options=contentwarehouse.TextTypeOptions(),
    )

    # Define Update Document Schema Request
    update_document_schema_request = contentwarehouse.UpdateDocumentSchemaRequest(
        name=document_schema_path,
        document_schema=contentwarehouse.DocumentSchema(
            display_name="My Test Schema",
            property_definitions=[updated_property_definition],
        ),
    )

    # Update Document schema
    updated_document_schema = document_schema_client.update_document_schema(
        request=update_document_schema_request
    )

    # Read the output
    print(f"Updated Document Schema: {updated_document_schema}")
