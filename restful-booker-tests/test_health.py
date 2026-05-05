"""Tests for the API's health and basic availability."""
import httpx
import pytest

# basic endpoint statuses
@pytest.mark.parametrize ("endpoint_status, expected", [
    pytest.param("/Hamburger", 404, id="invalid endpoint"),
    pytest.param("/ping", 200, marks=pytest.mark.xfail(reason="known issue, health checks should be 200")),
    pytest.param("/ping", 201, id="ping works despite unconventional status code"),
    pytest.param("/booking", 200),
    # add other enpoints as they come up
])
def test_endpoint_status(client, endpoint_status, expected):
    assert client.get(endpoint_status).status_code ==expected

# CRUD statuses (see conftest for fixture definitions)
def test_create_booking_status(shared_booking):
    assert shared_booking.status_code == 200

def test_retrieve_booking_status(shared_booking_from_server) :
    assert shared_booking_from_server.status_code == 200

# sanity check: check if the values match what they're supposed to be
# see conftest.py for expected values
@pytest.mark.parametrize ("shared_booking_field, expected", [
    pytest.param("firstname", "Test"),
    pytest.param("lastname", "User"),
    pytest.param("totalprice", 100),
    pytest.param("depositpaid", True),
    pytest.param("additionalneeds", "Breakfast")
])
def test_create_booking_faithfulness(shared_booking, shared_booking_field, expected):
    output = shared_booking.json()['booking'][shared_booking_field]
    assert output ==expected

# the schema is slightly different for the retrieved ones vs the created ones
@pytest.mark.parametrize ("shared_booking_field, expected", [
    pytest.param("firstname", "Test"),
    pytest.param("lastname", "User"),
    pytest.param("totalprice", 100),
    pytest.param("depositpaid", True),
    pytest.param("additionalneeds", "Breakfast")
])
def test_get_booking_faithfulness(shared_booking_from_server, shared_booking_field, expected):
    output = shared_booking_from_server.json()[shared_booking_field]
    assert output ==expected





    