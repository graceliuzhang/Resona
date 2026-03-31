import httpx
from config import LASTFM_KEY, LASTFM_SECRET

LASTFM_API_KEY = LASTFM_KEY
LASTFM_BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_artist_genres(artist_name: str) -> list[str]:
    response = httpx.get(LASTFM_BASE_URL, params={
        "method": "artist.getTopTags",
        "artist": artist_name,
        "api_key": LASTFM_API_KEY,
        "format": "json"
    })
    tags = response.json().get("toptags", {}).get("tag", [])
    return [tag["name"].lower() for tag in tags[:5]]