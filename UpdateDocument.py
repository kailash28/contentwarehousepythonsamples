
from google.cloud import contentwarehouse


def updateDocumentById(project_number: str, location: str, user_id: str , documentId:str ,schemaId:str) -> None:

    document_client = contentwarehouse.DocumentServiceClient()

    parent = document_client.common_location_path(
        project=project_number, location=location
    )

    document = contentwarehouse.Document()
    document.plain_text = "plain_text_value"
    #document.raw_document_path = "raw_document_path_value"
    document.display_name = "updated_document_name"
    document.document_schema_name ="projects/"+project_number+"/locations/"+location+"/documentSchemas/"+schemaId

    # Define Request
    update_document_By_Id_request = contentwarehouse.UpdateDocumentRequest(
        name="projects/" + project_number + "/locations/" + location + "/documents/" + documentId,
        document=document,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Create a Document for the given schema
    response = document_client.update_document(request=update_document_By_Id_request)
    return response

def updateDocumentByRefId(project_number: str, location: str, user_id: str , documentRefId:str , schemaId:str) -> None:

    document_client = contentwarehouse.DocumentServiceClient()

    parent = document_client.common_location_path(
        project=project_number, location=location,
    )
    document = contentwarehouse.Document()
    document.plain_text = "plain_text_value"
    #document.raw_document_path = "raw_document_path_value"
    document.display_name = "display_name_value"
    document.document_schema_name = "projects/" + project_number + "/locations/" + location + "/documentSchemas/" + schemaId
    # Define Request
    update_document_By_ref_Id_request = contentwarehouse.UpdateDocumentRequest(
        name="projects/"+project_number+"/locations/"+location+"/documents/referenceId/"+documentRefId,
        document=document,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Create a Document for the given schema
    response = document_client.update_document(request=update_document_By_ref_Id_request)
    return response

