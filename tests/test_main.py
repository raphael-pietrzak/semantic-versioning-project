from src.main import app
import json


def test_index_route():
    """Test de la route principale."""
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["name"] == "Main"
    assert data["version"] == "1.0.0"


def test_add_route():
    """Test de la route d'addition."""
    client = app.test_client()

    response1 = client.get("/add/2/3")
    data1 = json.loads(response1.data)
    response2 = client.get("/add/-1/1")
    data2 = json.loads(response2.data)
    response3 = client.get("/add/0/0")
    data3 = json.loads(response3.data)

    assert response1.status_code == 200
    assert data1["result"] == 5
    assert data2["result"] == 0
    assert data3["result"] == 0
