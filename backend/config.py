import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
# Backward compatible fallback for older env key names.
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI") or os.getenv("REDIRECT_URI")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

LASTFM_KEY = os.getenv("LASTFM_KEY")
LASTFM_SECRET = os.getenv("LASTFM_SECRET")