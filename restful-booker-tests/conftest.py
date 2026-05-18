"""Shared fixtures for the Restful-Booker test suite."""

import httpx
import pytest
import helpers as h
import test_data as d

# --- FIELDS --- #

BASE_URL = "https://restful-booker.herokuapp.com"

# --- FUNDAMENTAL FIXTURES --- #
@pytest.fixture(scope="session")
def client_no_auth() :
    """default client that does not have preconfigured auth"""
    with httpx.Client(base_url=BASE_URL, 
                      timeout=10.0
                      ) as client:
        yield client

@pytest.fixture(scope="session")
def client(auth_token) :
    """a client that has preconfigured auth"""
    with httpx.Client(base_url=BASE_URL, 
                      timeout=10.0, 
                      cookies={"token" : auth_token},
                      ) as client:
        yield client

# --- AUTH
@pytest.fixture(scope="session")
def auth_token(client_no_auth):
    response = client_no_auth.post("/auth", json={"username":"admin", "password":"password123"})
    assert response.status_code == 200, f"Auth failed: {response.text}"
    return response.json()["token"]

# --- CRUD --- #
@pytest.fixture(scope="module")
def shared_booking(client):
    # set up and validate
    booking = h.create_booking(client)
    assert booking.status_code == 200
    booking_id = h.find_booking_id(booking)
    # ---
    yield booking
    # clean up and validate
    is_deleted = h.find_booking(client, booking_id).status_code == 404
    if not is_deleted :
        assert h.delete_booking(client, booking_id).status_code in [200, 201, 204]
        assert h.find_booking(client, booking_id).status_code == 404
    else: assert True
    
@pytest.fixture (scope="module")
def shared_booking_from_server(client, shared_booking) :
    new_booking = shared_booking
    booking_id = h.find_booking_id(new_booking)
    r = h.find_booking(client, booking_id)
    assert r.status_code == 200
    return r

@pytest.fixture
def fresh_booking(client):
    """A booking unique to this test: safe to mutate"""
    booking = h.create_booking(client)
    assert booking.status_code ==200
    booking_id = h.find_booking_id(booking)
    # ---
    yield booking
    # ---
     # clean up and validate
    is_deleted = h.find_booking(client, booking_id).status_code == 404
    if not is_deleted :
        assert h.delete_booking(client, booking_id).status_code in [200, 201, 204]
        assert h.find_booking(client, booking_id).status_code == 404
    else: assert True