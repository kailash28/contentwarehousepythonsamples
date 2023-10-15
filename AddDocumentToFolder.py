

from google.cloud import contentwarehouse_v1
from google.cloud import contentwarehouse

def add_to_folder(project_number:str , location:str , user_id:str ,folderId:str, docId:str):
    # Create a client

    client = contentwarehouse_v1.DocumentLinkServiceClient()
    # Initialize request argument(s)
    folderName = "projects/"+project_number+"/locations/"+location+"/documents/"+folderId
    docName = "projects/"+project_number+"/locations/"+location+"/documents/"+docId
    link = contentwarehouse.DocumentLink()
    link.source_document_reference = contentwarehouse_v1.DocumentReference()
    link.source_document_reference.document_name = folderName

    link.target_document_reference = contentwarehouse_v1.DocumentReference()
    link.target_document_reference.document_name = docName

    print(folderName)
    print(link.target_document_reference.document_name)


    request = contentwarehouse_v1.CreateDocumentLinkRequest(
        parent=folderName,
        document_link=link,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
    )

    # Make the request
    return client.create_document_link( request=request)
	
