"""
Manage SSH keys on Digital Ocean
"""


def create_ssh_key(key_name: str, public_key_str: str):
    """https://docs.digitalocean.com/reference/api/api-reference/#operation/sshKeys_create"""


def delete_key(id: int):
    """https://docs.digitalocean.com/reference/api/api-reference/#operation/sshKeys_delete"""


def retrieve_ssh_key(id: int):
    """https://docs.digitalocean.com/reference/api/api-reference/#operation/sshKeys_get"""
