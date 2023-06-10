"""
All requests belongs to Asana API:
https://developers.asana.com/reference/rest-api-reference
"""
import asana
from .models import Employee


def invite_user_to_asana(user: Employee):
    """
    Invite user to organization.
    Developer documentation: https://developers.asana.com/reference/adduserforworkspace
    """
    workspace_gid = "123"
    client = asana.Client.access_token("PERSONAL_ACCESS_TOKEN")
    result = client.workspaces.add_user_for_workspace(
        workspace_gid, {"email": user.email}, opt_pretty=True
    )
