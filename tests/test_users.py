from app import schemas
from .database import client, session
from app.config import settings
import pytest
from jose import jwt


@pytest.fixture
def test_user(client):
    user_data = {"email": "ali@gmail.com",
                 "password": "password123"}
    response = client.post("/users/", json=user_data)
    
    assert response.status_code == 201
    print(response.json())
    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user
        
        
def test_create_user(client):
    response = client.post("/users/", json={
        "email": "hello123@gmail.com",
        "password": "password123"
    })
    new_user = schemas.UserOut(**response.json())
    
    assert new_user.email == "hello123@gmail.com"
    assert response.status_code == 201
    
    
def test_login_user(client, test_user):
    response = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert response.status_code == 200
    
    