import requests

def get_authorization_url(client_id, redirect_uri):
    return f"https://api.fyers.in/api/v3/generate-authcode?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state=sample"

def exchange_code_for_token(client_id, secret_id, redirect_uri, auth_code):
    url = "https://api.fyers.in/api/v3/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "secret_key": secret_id,
        "code": auth_code,
        "redirect_uri": redirect_uri
    }
    response = requests.post(url, json=payload)
    return response.json()