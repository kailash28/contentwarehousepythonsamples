
from google.cloud import contentwarehouse_v1

def remove_doc_from_folder_with_link_id(project_number:str , location:str , user_id:str ,folder_id:str ,link:str):
    # Create a client
    client = contentwarehouse_v1.DocumentLinkServiceClient()

    linkName = "projects/" + project_number + "/locations/" + location + "/documents/" + folder_id+"/documentLinks/"+link
    # Initialize request argument(s)
    request = contentwarehouse_v1.DeleteDocumentLinkRequest(
        name=linkName,
        request_metadata=contentwarehouse_v1.RequestMetadata(
            user_info=contentwarehouse_v1.UserInfo(id=user_id)
        ),
    )

    # Make the request
    return client.delete_document_link(request=request)
