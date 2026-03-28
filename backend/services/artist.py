from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import httpx
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
from token_store import token_store
from main import app

@app.get("/top-artists")
async def get_top_artists(n: int = 10, time_range: str = "medium_term"):
    access_token = token_store.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated.")

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.spotify.com/v1/me/top/artists",
            headers={"Authorization": f"Bearer {access_token}"},
            params={"limit": n, "time_range": time_range},
        )

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Spotify API error")

    data = response.json()
    return {
        "top_artists": [
            {
                "rank": i + 1,
                "name": a["name"],
                "genres": a["genres"],
                "popularity": a["popularity"],
                "url": a["external_urls"]["spotify"],
            }
            for i, a in enumerate(data["items"])
        ]
    }