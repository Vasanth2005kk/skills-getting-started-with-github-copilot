from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_get_activities_returns_activity_list():
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]


def test_signup_for_activity_rejects_duplicate_email():
    duplicate_email = "michael@mergington.edu"

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": duplicate_email},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"
