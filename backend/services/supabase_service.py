from supabase import create_client
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