"""Tests for PUT and PATCH operations on bookings."""
import helpers as h
import test_data as d

def test_put_replaces_all_fields(client, fresh_booking):
    """PUT with a complete booking body replaces all fields"""
    booking_id = h.find_booking_id(fresh_booking)
    response = h.put_booking(client, booking_id)
    assert response.status_code ==200

    fetched = h.find_booking(client, booking_id)
    assert fetched.status_code ==200
    assert fetched.json()["firstname"] == d.UPDATED_VALID_B_INFO["firstname"]
    assert fetched.json()["totalprice"] == d.UPDATED_VALID_B_INFO["totalprice"]

def test_patch_replaces_only_targeted_field(client, fresh_booking):
    booking_id = h.find_booking_id(fresh_booking)
    json_updates = {"firstname" : d.UPDATED_VALID_B_INFO["firstname"],}
    response = h.patch_booking(client, booking_id, json_updates)
    assert response.status_code == 200

    fetched = h.find_booking(client, booking_id)
    assert fetched.json()["firstname"] == d.UPDATED_VALID_B_INFO["firstname"]
    assert fetched.json()["totalprice"] == d.DEFAULT_VALID_B_INFO["totalprice"]
