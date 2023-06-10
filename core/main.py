import requests
from models import Employee


def create_employee(email: str, username: str) -> Employee:
    """Store newly created organization user"""
    return Employee(email=email, username=username)


def invite_github_user_to_organization(user: Employee):
    """Add user to github company.
    API Documentation:
        https://docs.github.com/en/rest/orgs/members?apiVersion=2022-11-28#create-an-organization-invitation
    Organization owner only.
    """
    org_name = "abc"  # get organization name
    # get organization token from secure storage ( unpack hashed value with
    # one time password or with SMS )
    org_token = "org_token"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {org_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    request_body = {
        "email": "octocat@github.com",
        "role": "direct_member",
        "team_ids": [12, 26],
    }
    request = requests.post(
        f"https://api.github.com/orgs/{org_name}/invitations",
        headers=headers,
        json=request_body,
    )
    print(request.json())


if __name__ == "__main__":
    emp: Employee = create_employee("test@test.com", "test_emp")
    print(emp)
