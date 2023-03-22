from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == [{"first_name": "Frank", "last_name": "Appau",
                                "email": "frankappau@gmail.com", "id": 3, "is_active": true}]


# def test_login():
#     response = client.post('/login', headers={"X-Token": "coneofsilence"}, json={"email": "appausamuel90@gmail.com", "password": "sammy!202738"},
#                            )
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [{
#         "detail": "string",
#         "result": "string"
#     }]


# def test_create_users():
#     response = client.post('/')
#     assert response.status_code == 200
#     assert response.json() == {
#   "first_name": "string",
#   "last_name": "string",
#   "email": "string",
#   "id": 0,
#   "is_active": true
# }


# def test_get_user():
#     response = client.get('/1/')
#     assert response.status_code == 200
#     assert response.json() == {
#         "first_name": "string",
#         "last_name": "string",
#         "email": "string",
#         "id": 0,
#         "is_active": true
#     }

# def test_update_user():
#     response = client.patch('/')
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() =={
#   "detail": "string",
#   "result": "string"
# }


# # def test_delete_user():
# #     response = client.delete('/delete/1')
# #     assert response.status_code == 200
# #     assert response.json() == {
#   "detail": "string",
#   "result": "string"
# }
