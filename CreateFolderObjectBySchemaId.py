

from google.cloud import contentwarehouse
import os
import GetSchemaById

def createFolderObejectByFolderSchemaId(project_number: str, location: str, user_id: str , folderSchemaId:str) -> None:

    document_schema = GetSchemaById.get_document_schema_by_id(project_number , location , folderSchemaId)

    # Create a Document Service client
    document_client = contentwarehouse.DocumentServiceClient()

    # The full resource name of the location, e.g.:
    # projects/{project_number}/locations/{location}
    parent = document_client.common_location_path(
        project=project_number, location=location
    )
    # Define Document
    document = contentwarehouse.Document(
        #display_name="My Test Document",
        document_schema_name=document_schema.name
        #raw_document_path = "gs://dbecm-bucket/TestDoc_1.5MB.pdf"
        #plain_text="This is a sample of a document's text.",
        #properties=[document_property],
    )

    # Define Request
    create_document_request = contentwarehouse.CreateDocumentRequest(
        parent=parent,
        document=document,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Create a Document for the given schema
    response = document_client.create_document(request=create_document_request)
    return response


