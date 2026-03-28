

def extract_genres_from_artists(artists: list[dict]) -> list[str]:
    genres = []
    for artist in artists:
        genres.extend(artist["genres"])
    return list(set(genres))