import os
import requests



CORE_PATH = os.get("CORE_PATH")

def get_employers():
    resp = requests.get(f"{CORE_PATH}/employers")
    if resp.status_code > 200:
        return None
    return resp.json()