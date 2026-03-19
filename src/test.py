import sys
import os
sys.path.append(os.path.dirname(__file__))

from tejasa import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_add_api():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    data = response.get_json()
    assert data["result"] == 5
