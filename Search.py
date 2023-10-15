

from google.cloud import contentwarehouse


def search(project_number: str, location: str, user_id: str, searchQuery: str) -> None:

    document_client = contentwarehouse.DocumentServiceClient()

    parent = document_client.common_location_path(
        project=project_number, location=location
    )
    # Define Request
    search_document_request = contentwarehouse.SearchDocumentsRequest(
        parent=parent,
        request_metadata=contentwarehouse.RequestMetadata(
            user_info=contentwarehouse.UserInfo(id=user_id)
        ),
        document_query=contentwarehouse.DocumentQuery(
            query=searchQuery,
            is_nl_query=0,
            document_creator_filter=user_id
        ),
        offset=0,
        page_size=100,
        require_total_size=1,
        total_result_size=2
    )

    # Create a Document for the given schema
    response = document_client.search_documents(request=search_document_request)
    return response

