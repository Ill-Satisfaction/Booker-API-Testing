import helpers as h
import test_data as d
import pytest



""" covered by status codes
# Smoke Create -> Delete
def test_smoke_create_then_delete_booking (client) :
    # create and verify created
    booking = h.create_booking(client)
    booking_id = h.find_booking_id(booking)
    assert h.find_booking(client, booking_id).status_code == 200
    # delete and verify gone
    h.delete_booking(client, booking_id)
    assert h.find_booking(client, booking_id).status_code == 404
"""


# verify delete works
def test_fetching_deleted_booking_returns_404 (client, fresh_booking):
    b_id = h.find_booking_id(fresh_booking)
    h.delete_booking(client, b_id)
    assert h.find_booking(client, b_id).status_code == 404


## MORE IN-DEPTH TESTING
# CREATE BOOKING
@pytest.mark.parametrize ("shared_booking_field", [
    pytest.param("firstname"),
    pytest.param("lastname"),
    pytest.param("totalprice"),
    pytest.param("depositpaid"),
    pytest.param("additionalneeds"),
    pytest.param("bookingdates"),
])
def test_smoke_create_booking_correct_vals (shared_booking, shared_booking_field) :
    assert d.DEFAULT_VALID_B_INFO[shared_booking_field] == shared_booking.json()['booking'][shared_booking_field]

# RETRIEVE BOOKING
# the schema is slightly different for the retrieved ones vs the created ones
@pytest.mark.parametrize ("shared_booking_field", [
    pytest.param("firstname"),
    pytest.param("lastname"),
    pytest.param("totalprice"),
    pytest.param("depositpaid"),
    pytest.param("additionalneeds"),
    pytest.param("bookingdates"),
])
def test_smoke_retrieve_booking_correct_vals(shared_booking_from_server, shared_booking_field):
    assert d.DEFAULT_VALID_B_INFO[shared_booking_field] == shared_booking_from_server.json()[shared_booking_field]

# PUT BOOKING
def test_put_replaces_all_fields(client, fresh_booking):
    """PUT with a complete booking body replaces all fields"""
    booking_id = h.find_booking_id(fresh_booking)
    h.put_booking(client, booking_id)
    fetched = h.find_booking(client, booking_id).json()
    assert fetched["firstname"] == d.UPDATED_VALID_B_INFO["firstname"]
    assert fetched["totalprice"] == d.UPDATED_VALID_B_INFO["totalprice"]

# PATCH BOOKING
def test_patch_replaces_only_targeted_field(client, fresh_booking):
    booking_id = h.find_booking_id(fresh_booking)
    h.patch_booking(client, booking_id, d.VALID_FIRSTNAME_JSON_PATCH)
    fetched = h.find_booking(client, booking_id).json()
    assert fetched["firstname"] == d.UPDATED_VALID_B_INFO["firstname"]
    assert fetched["totalprice"] == d.DEFAULT_VALID_B_INFO["totalprice"]