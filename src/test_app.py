import sys
import os

# VERY IMPORTANT (fix import in GitHub Actions)
sys.path.append(os.path.dirname(__file__))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.get_json()["result"] == 5
