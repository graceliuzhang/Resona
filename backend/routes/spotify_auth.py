from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from services.spotify_service import (
    get_auth_url,
    exchange_code_for_token,
    get_user_profile,
    get_top_artists
)

from services.supabase_service import insert_user

router = APIRouter()


@router.get("/login")
def spotify_login():

    url = get_auth_url()

    return RedirectResponse(url)


@router.get("/callback")
def spotify_callback(code: str):

    token_data = exchange_code_for_token(code)

    access_token = token_data["access_token"]
    refresh_token = token_data["refresh_token"]

    profile = get_user_profile(access_token)

    artists = get_top_artists(access_token)

    genres = []
    for artist in artists["items"]:
        genres.extend(artist["genres"])

    user_data = {
        "spotify_id": profile["id"],
        "display_name": profile["display_name"],
        "email": profile["email"],
        "avatar_url": profile["images"][0]["url"] if profile["images"] else None,
        "top_artists": artists["items"],
        "genres": list(set(genres)),
        "access_token": access_token,
        "refresh_token": refresh_token
    }

    insert_user(user_data)

    return {"message": "User stored successfully"}