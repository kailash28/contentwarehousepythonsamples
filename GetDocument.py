
from google.cloud import contentwarehouse


def getDocumentById(project_number: str, location: str, user_id: str , documentId:str) -> None:

    document_client = contentwarehouse.DocumentServiceClient()

    parent = document_client.common_location_path(
        project=project_number, location=location
    )
    # Define Request
    get_document_By_Id_request = contentwarehouse.GetDocumentRequest(
        #parent=parent,
        name="projects/"+project_number+"/locations/"+location+"/documents/"+documentId,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Create a Document for the given schema
    response = document_client.get_document(request=get_document_By_Id_request)
    return response

def getDocumentByRefId(project_number: str, location: str, user_id: str , documentRefId:str) -> None:

    document_client = contentwarehouse.DocumentServiceClient()

    parent = document_client.common_location_path(
        project=project_number, location=location,
    )
    # Define Request
    get_document_By_ref_Id_request = contentwarehouse.GetDocumentRequest(
        name="projects/"+project_number+"/locations/"+location+"/documents/referenceId/"+documentRefId,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Create a Document for the given schema
    response = document_client.get_document(request=get_document_By_ref_Id_request)
    return response
	
