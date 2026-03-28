import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from main import app

client = TestClient(app)

MOCK_ARTISTS_RESPONSE = {
    "items": [
        {
            "name": "Artist One",
            "genres": ["pop", "dance"],
            "popularity": 90,
            "external_urls": {"spotify": "https://spotify.com/artist1"}
        },
        {
            "name": "Artist Two",
            "genres": ["rock"],
            "popularity": 80,
            "external_urls": {"spotify": "https://spotify.com/artist2"}
        },
    ]
}

@pytest.fixture(autouse=True)
def mock_token():
    # Bypasses the token check entirely
    with patch("token_store.token_store", {"access_token": "fake_token"}):
        yield

@patch("services.spotify.httpx.AsyncClient")
def test_get_top_artists(mock_client):
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_ARTISTS_RESPONSE

    mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)

    response = client.get("/top-artists?n=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data["top_artists"]) == 2
    assert data["top_artists"][0]["name"] == "Artist One"
    assert data["top_artists"][0]["rank"] == 1