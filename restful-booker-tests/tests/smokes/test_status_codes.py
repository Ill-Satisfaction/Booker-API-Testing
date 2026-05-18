import helpers as h
import test_data as d
import pytest

# --- VALID ATTEMPTS --- #
# CRU statuses (see conftest for fixture definitions)
def test_valid_create_returns_200 (shared_booking):
    assert shared_booking.status_code == 200

def test_valid_retrieve_returns_200(shared_booking_from_server) :
    assert shared_booking_from_server.status_code == 200

def test_valid_put_returns_200(client, fresh_booking) :
    assert h.put_booking(client, h.find_booking_id(fresh_booking)).status_code == 200

def test_valid_patch_returns_200(client, fresh_booking) :
    assert h.patch_booking(client, h.find_booking_id(fresh_booking), d.VALID_FIRSTNAME_JSON_PATCH).status_code == 200

@pytest.mark.xfail(reason="Booker API deletes as 201, when standard would be 200 or 204")
def test_valid_delete_returns_standard_code(client, fresh_booking) :
    b_id = h.find_booking_id(fresh_booking)
    assert h.delete_booking(client, b_id).status_code in [200, 204]

def test_valid_delete_returns_201(client, fresh_booking) :
    b_id = h.find_booking_id(fresh_booking)
    assert h.delete_booking(client, b_id).status_code == 201