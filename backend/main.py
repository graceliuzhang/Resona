from fastapi import FastAPI
from routes import spotify_auth, rooms
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.include_router(spotify_auth.router, prefix="/auth")

app.include_router(rooms.router, prefix="/rooms")