def extract_genres_from_artists(artists):
    genres = []
    for artist in artists:
        # use .get and ensure it's a list
        artist_genres = artist.get("genres") or []
        if isinstance(artist_genres, list):
            genres.extend(artist_genres)
    return genres