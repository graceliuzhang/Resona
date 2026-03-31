from fastapi import APIRouter
from services.room_service import (
    create_room,
    get_all_rooms,
    join_room,
    leave_room,
    get_room_members
)

router = APIRouter()


# Get all rooms
@router.get("/")
def list_rooms():
    rooms = get_all_rooms()
    return {"rooms": rooms}

@router.post("/create")
def create(name: str, genre_tags: list[str], host_id: str):

    room = create_room(name, genre_tags, host_id)

    return {
        "message": "room created",
        "room": room
    }


# Join a room
@router.post("/join")
def join(room_id: str, user_id: str):
    data = join_room(room_id, user_id)
    return {"message": "joined room", "data": data}


# Leave a room
@router.post("/leave")
def leave(room_id: str, user_id: str):
    data = leave_room(room_id, user_id)
    return {"message": "left room", "data": data}


# Get members in a room
@router.get("/members")
def members(room_id: str):
    members = get_room_members(room_id)
    return {"members": members}