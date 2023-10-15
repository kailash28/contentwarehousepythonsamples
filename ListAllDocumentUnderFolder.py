
from google.cloud import contentwarehouse_v1

def list_sub_docs(project_number:str , location:str , user_id:str ,folderId:str):
    # Create a client
    folderName = "projects/" + project_number + "/locations/" + location + "/documents/" + folderId
    client = contentwarehouse_v1.DocumentLinkServiceClient()

    # Initialize request argument(s)
    request = contentwarehouse_v1.ListLinkedTargetsRequest(
        parent=folderName,
        request_metadata=contentwarehouse_v1.RequestMetadata(
            user_info=contentwarehouse_v1.UserInfo(id=user_id)
        ),
    )

    # Make the request
    return client.list_linked_targets(request=request)

