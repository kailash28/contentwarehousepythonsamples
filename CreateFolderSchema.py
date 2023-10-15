
from google.cloud import contentwarehouse_v1

def create_folder_schema(project_number :str, location:str, folderName :str ):
    # Create a client
    client = contentwarehouse_v1.DocumentSchemaServiceClient()

    # Initialize request argument(s)
    document_schema = contentwarehouse_v1.DocumentSchema()
    document_schema.display_name = folderName
    document_schema.document_is_folder = True

    request = contentwarehouse_v1.CreateDocumentSchemaRequest(
        parent="projects/"+project_number+"/locations/"+location,
        document_schema=document_schema,
    )

    # Make the request
    return client.create_document_schema(request=request)

