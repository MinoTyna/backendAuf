import base64
import requests

CLIENT_ID = "4GUDn93Kywn57rS93Mrq3dz30UZL9AJ3"
CLIENT_SECRET = "l1VtDjY10FI7O72c5EB3SjIw5pY9sWLDLILSG3OibSY9"

def get_access_token():
    url = "https://api.orange.com/oauth/v3/token"

    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_base64 = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=data, headers=headers)
    token = response.json().get("access_token")
    
    return token
