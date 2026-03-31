from fastapi import FastAPI
from routes import spotify_auth, rooms

app = FastAPI()

app.include_router(spotify_auth.router, prefix="/auth")
app.include_router(rooms.router, prefix="/rooms")