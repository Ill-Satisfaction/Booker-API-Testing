import pytest
import helpers as h
import test_data as d


# bad booking ID
def test_invalid_retrieve_returns_404(client) :
    assert h.find_booking(client, d.INVALID_BOOKING_ID).status_code == 404

@pytest.mark.xfail(reason="404 is typical for a missing resource")
def test_invalid_put_returns_404(client) :
    assert h.put_booking(client, d.INVALID_BOOKING_ID).status_code == 404

@pytest.mark.xfail(reason="404 is typical for a missing resource")
def test_invalid_patch_returns_404(client) :
    assert h.patch_booking(client, d.INVALID_BOOKING_ID, d.VALID_FIRSTNAME_JSON_PATCH).status_code == 404

def test_invalid_put_returns_405(client) :
    assert h.put_booking(client, d.INVALID_BOOKING_ID).status_code == 405

def test_invalid_patch_returns_405(client) :
    assert h.patch_booking(client, d.INVALID_BOOKING_ID, d.VALID_FIRSTNAME_JSON_PATCH).status_code == 405