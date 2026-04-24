import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath("app"))

from app import app

app.config["TESTING"] = True


def test_home_page():
    with patch("routes.Task") as mock_task:
        mock_task.query.all.return_value = []

        client = app.test_client()
        response = client.get("/")

        assert response.status_code == 200
        assert "Список задач".encode("utf-8") in response.data