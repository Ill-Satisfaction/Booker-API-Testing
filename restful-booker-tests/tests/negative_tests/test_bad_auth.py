import pytest
import test_data as d
import helpers as h

# no auth
@pytest.mark.xfail(reason="known issue: auth is not needed to create new bookings in Booker")
def test_no_auth_create_returns_403 (client_no_auth):
    assert h.create_booking(client_no_auth).status_code == 403

def test_no_auth_create_returns_200 (client_no_auth):
    assert h.create_booking(client_no_auth).status_code == 200

def test_no_auth_retrieve_returns_200(client_no_auth, shared_booking) :
    b_id = h.find_booking_id(shared_booking)
    assert h.find_booking(client_no_auth, b_id).status_code == 200

def test_no_auth_put_returns_403(client_no_auth, fresh_booking) :
    assert h.put_booking(client_no_auth, h.find_booking_id(fresh_booking)).status_code == 403

def test_no_auth_patch_returns_403(client_no_auth, fresh_booking) :
    assert h.patch_booking(client_no_auth, h.find_booking_id(fresh_booking), d.VALID_FIRSTNAME_JSON_PATCH).status_code == 403

def test_no_auth_delete_returns_403(client_no_auth, fresh_booking) :
    b_id = h.find_booking_id(fresh_booking)
    assert h.delete_booking(client_no_auth, b_id).status_code == 403

@pytest.mark.xfail(reason="401 is typical for a missing auth token")
def test_no_auth_put_returns_401(client_no_auth, fresh_booking) :
    assert h.put_booking(client_no_auth, h.find_booking_id(fresh_booking)).status_code == 401

@pytest.mark.xfail(reason="401 is typical for a missing auth token")
def test_no_auth_patch_returns_401(client_no_auth, fresh_booking) :
    assert h.patch_booking(client_no_auth, h.find_booking_id(fresh_booking), d.VALID_FIRSTNAME_JSON_PATCH).status_code == 401

@pytest.mark.xfail(reason="401 is typical for a missing auth token")
def test_no_auth_delete_returns_401(client_no_auth, fresh_booking) :
    b_id = h.find_booking_id(fresh_booking)
    assert h.delete_booking(client_no_auth, b_id).status_code == 401