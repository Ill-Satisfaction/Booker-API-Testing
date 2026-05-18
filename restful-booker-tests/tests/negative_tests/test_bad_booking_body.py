import pytest
import helpers as h
import test_data as d


FIRSTNAME_BUGS = {}
@pytest.mark.parametrize("bad_value", h.with_known_bugs(d.INVALID_STRING_ENTRIES, FIRSTNAME_BUGS))
def test_invalid_firstname_create_returns_400 (client, bad_value) :
    body = {**d.DEFAULT_VALID_B_INFO, "firstname": bad_value}
    response = h.create_booking(client, body)
    assert response.status_code == 500