"""Shared fixtures for the Restful-Booker test suite."""

import httpx
import pytest
import helpers as h

# --- FIELDS --- #

BASE_URL = "https://restful-booker.herokuapp.com"

# --- FUNDAMENTAL FIXTURES --- #

@pytest.fixture(scope="session")
def auth_token(client):
    response = client.post("/auth", json={"username":"admin", "password":"password123"})
    assert response.status_code == 200, f"Auth failed: {response.text}"
    return response.json()["token"]

@pytest.fixture(scope="session")
def client() :
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        yield client

# --- CRUD --- #

@pytest.fixture(scope="module")
def shared_booking(client, auth_token):
    # set up and validate
    booking = h.create_booking(client)
    assert booking.status_code == 200
    booking_id = h.find_booking_id(booking)
    # ---
    yield booking
    # clean up and validate
    deletion = h.delete_booking(client, auth_token, booking_id)
    assert deletion.status_code in [200, 201, 204]
    assert h.find_booking(client, booking_id) == 404
    
@pytest.fixture (scope="module")
def shared_booking_from_server(client, shared_booking) :
    new_booking = shared_booking
    booking_id = h.find_booking_id(new_booking)
    r = h.find_booking(client, booking_id)
    r.status_code == 200
    return r