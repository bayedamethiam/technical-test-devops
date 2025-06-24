import os
from unittest.mock import patch, MagicMock

import pytest
from httpx import AsyncClient, ASGITransport

os.environ["MONGO_URL"] = "mongodb://fake:27017"
os.environ["MONGO_DATABASE"] = "testdb"

from main import app # noqa


@pytest.mark.asyncio
async def test_create_message_success():
    test_input = {"message": "hello test"}

    with patch("main.collection.insert_one") as mock_insert:
        mock_insert.return_value = MagicMock()

        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/message", json=test_input)

        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "hello test"
        assert "identifier" in data
