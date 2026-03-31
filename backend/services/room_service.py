from services.supabase_service import supabase


def get_all_rooms():
    response = supabase.table("rooms").select("*").execute()
    return response.data

def create_room(name: str, genre_tags: list, host_id: str):

    room_data = {
        # delete id column in supabase and let the chart linked by host_id like the user id
        "name": name,
        "genre_tags": genre_tags,
        "host_id": host_id, # get user id from ?? spotify auth
        "current_track": None,
        "is_playing": False
    }

    response = supabase.table("rooms").insert(room_data).execute()

    return response.data


def join_room(room_id: str, user_id: str):

    data = {
        "room_id": room_id,
        "user_id": user_id
    }

    response = supabase.table("room_members").insert(data).execute()
    return response.data


def leave_room(room_id: str, user_id: str):

    response = (
        supabase.table("room_members")
        .delete()
        .eq("room_id", room_id)
        .eq("user_id", user_id)
        .execute()
    )

    return response.data


def get_room_members(room_id: str):

    response = (
        supabase.table("room_members")
        .select("*")
        .eq("room_id", room_id)
        .execute()
    )

    return response.data