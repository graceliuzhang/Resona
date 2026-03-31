from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from services.lastfm_service import get_artist_genres

from services.spotify_service import (
    get_auth_url,
    exchange_code_for_token,
    get_user_profile,
    get_top_artists
)
from services.supabase_service import insert_user, get_user
from services.genre import extract_genres_from_artists

router = APIRouter()


@router.get("/login")
def spotify_login():
    url = get_auth_url()
    return RedirectResponse(url)


@router.get("/callback")
def spotify_callback(code: str):
    try:
        token_data = exchange_code_for_token(code)
        access_token = token_data["access_token"]
        refresh_token = token_data["refresh_token"]

        profile = get_user_profile(access_token)
        artist_items = get_top_artists(access_token).get("items", [])

        top_artist_names = [artist["name"] for artist in artist_items[:3]]  # names only

        all_genres = []
        for name in top_artist_names:
            all_genres.extend(get_artist_genres(name))
        all_genres = list(set(all_genres))[:5] # deduplicate
        user_data = {
            "spotify_id": profile.get("id"),
            "display_name": profile.get("display_name"),
            "email": profile.get("email"),
            "top_artists": top_artist_names,  # names instead of full objects
            "genres": all_genres,
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        insert_user(user_data)
        return {"top_artists": top_artist_names, "genres": all_genres}
    except Exception as e:
        return {"error": str(e)}