from fastapi import FastAPI
from routes import spotify_auth

app = FastAPI()

app.include_router(spotify_auth.router, prefix="/auth")