import httpx

SPOTIFY_BASE = "https://api.spotify.com/v1"

async def search_tracks(query: str, token: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{SPOTIFY_BASE}/search",
            params={"q": query, "type": "track", "limit": 20},
            headers={"Authorization": f"Bearer {token}"}
        )
        return r.json()

async def play_track(track_uri: str, position_ms: int, token: str):
    async with httpx.AsyncClient() as client:
        await client.put(f"{SPOTIFY_BASE}/me/player/play",
            json={"uris": [track_uri], "position_ms": position_ms},
            headers={"Authorization": f"Bearer {token}"}
        )