from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_view_events():
    response = client.get("/api/v1/ticket/view-events")
    assert response.status_code == 200
    assert response.json() == [{"id":1,"name":"selorm","event":"UCL-final","creation_date":"2023-03-22T10:19:59.363000","modified_date":"2023-03-22T11:26:33.896724"}]


# client = TestClient(app)

def test_add_events():
    # Prepare the request data
    item = {"name": "gabriel", "event": "AXA"}

    # Send a POST request to the /items endpoint with the data
    response = client.post("/api/v1/ticket/create-event", json=item)
    print(response)
    # Assert that the response has a 200 OK status code
    assert response.status_code == 200

    # Assert that the response contains the expected data
    assert response.json() == {"name": "gabriel", "event": "AXA"}
