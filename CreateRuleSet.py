
from google.cloud import contentwarehouse


def create_rule_set(project_number: str, location: str) -> None:
    # Create a client
    client = contentwarehouse.RuleSetServiceClient()

    # The full resource name of the location, e.g.:
    # projects/{project_number}/locations/{location}
    parent = client.common_location_path(project=project_number, location=location)

    actions = contentwarehouse.Action(
        delete_document_action=contentwarehouse.DeleteDocumentAction(
            enable_hard_delete=True
        )
    )

    rules = contentwarehouse.Rule(
        trigger_type="ON_CREATE",
        condition="documentType == 'W9' && STATE =='CA'",
        actions=[actions],
    )

    rule_set = contentwarehouse.RuleSet(
        description="W9: Basic validation check rules.",
        source="My Organization",
        rules=[rules],
    )

    # Initialize request argument(s)
    request = contentwarehouse.CreateRuleSetRequest(parent=parent, rule_set=rule_set)

    # Make the request
    response = client.create_rule_set(request=request)

    # Handle the response
    print(f"Rule Set Created: {response}")

    # Initialize request argument(s)
    request = contentwarehouse.ListRuleSetsRequest(
        parent=parent,
    )

    # Make the request
    page_result = client.list_rule_sets(request=request)

    # Handle the response
    for response in page_result:
        print(f"Rule Sets: {response}")


