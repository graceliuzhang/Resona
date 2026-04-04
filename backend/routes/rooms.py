from fastapi import APIRouter, HTTPException, Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from services.supabase_service import (
    create_room,
    join_room,
    get_room,
    get_user,
)
router = APIRouter()
from services.spotify_service import get_user_profile

from pydantic import BaseModel

class CreateRoomRequest(BaseModel):
    genre: str

@router.post("/rooms")
def create_room_route(request: Request, body: CreateRoomRequest, access_token: str = None):
    token = access_token or request.session.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not logged in")
    profile = get_user_profile(token)
    host_id = profile["id"]
    room = create_room(host_id, body.genre)
    return {"room": room}

@router.post("/rooms/{room_id}/join")
def join_room_route(room_id: str, user_id: str):
    join_room(room_id, user_id)
    return {"message": "Joined room successfully"}

@router.get("/rooms/{room_id}")
def get_room_route(room_id: str):
    room = get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return {"room": room}