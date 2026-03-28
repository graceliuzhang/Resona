import requests
import base64
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI


def get_auth_url():

    scope = "user-read-email user-read-private user-top-read"

    return (
        "https://accounts.spotify.com/authorize"
        f"?client_id={SPOTIFY_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={SPOTIFY_REDIRECT_URI}"
        f"&scope={scope}"
    )


def exchange_code_for_token(code):

    url = "https://accounts.spotify.com/api/token"

    auth_str = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_bytes = auth_str.encode()
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": SPOTIFY_REDIRECT_URI
    }

    response = requests.post(url, headers=headers, data=data)

    return response.json()


def get_user_profile(access_token):

    headers = {"Authorization": f"Bearer {access_token}"}

    r = requests.get("https://api.spotify.com/v1/me", headers=headers)

    return r.json()


def get_top_artists(access_token):

    headers = {"Authorization": f"Bearer {access_token}"}

    r = requests.get(
        "https://api.spotify.com/v1/me/top/artists?limit=10",
        headers=headers
    )

    return r.json()