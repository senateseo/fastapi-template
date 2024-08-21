from fastapi.testclient import TestClient
from main import app, todos
client = TestClient(app)


def setup_function():
    todos.clear()

def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    response = client.post("/", json={"name": "sangwon", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "sangwon", "completed": False}
    
def test_update_todo():
    client.post("/", json={"name": "sangwon", "completed": False})
    response = client.put("/1", json={"name": "paul", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "paul", "completed": True}
    

def test_delete_todo():
    client.post("/", json={"name": "sangwon", "completed": False})
    response = client.delete("/1")
    
    assert response.status_code == 200
    assert response.json() == {"name": "sangwon", "completed": False}