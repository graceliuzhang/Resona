from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_user(user_data):
    response = supabase.table("users").upsert(user_data).execute()
    return response