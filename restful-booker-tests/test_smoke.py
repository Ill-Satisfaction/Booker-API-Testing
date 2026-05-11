import helpers as h
import pytest

def test_smoke_create_then_delete_booking (client, auth_token) :
    # create and verify created
    booking = h.create_booking(client)
    booking_id = h.find_booking_id(booking)
    assert h.find_booking(client, booking_id).status_code == 200
    # delete and verify gone
    h.delete_booking(client, auth_token, booking_id)
    assert h.find_booking(client, booking_id).status_code == 404
