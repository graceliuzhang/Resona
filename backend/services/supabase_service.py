from supabase import create_client
from fastapi import APIRouter, HTTPException, Request
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_user(user_data):
    response = (
        supabase
        .table("users")
        .upsert(user_data, on_conflict="spotify_id")
        .execute()
    )
    return response

def get_user(spotify_id: str):
    response = supabase.table("users").select("genres").eq("spotify_id", spotify_id).single().execute()
    return response.data

def create_room(host_id: str, genre: str):
    response = supabase.table("rooms").insert({
        "host_id": host_id,
        "genre": genre,
    }).execute()
    return response.data[0]

def get_room(room_id: str):
    response = supabase.table("rooms")\
        .select("*, room_participants(*)")\
        .eq("id", room_id)\
        .single()\
        .execute()
    return response.data

def join_room(room_id: str, user_id: str):
    room = get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    if len(room["room_participants"]) >= room["max_participants"]:
        raise HTTPException(status_code=400, detail="Room is full")
    
    supabase.table("room_participants").insert({
        "room_id": room_id,
        "user_id": user_id
    }).execute()