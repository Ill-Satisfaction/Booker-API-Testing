import pytest


# BASIC DATA
INVALID_BOOKING_ID = -1337

DEFAULT_VALID_B_INFO = {
    "firstname": "Test",
    "lastname": "User",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-12-01",
        "checkout": "2026-12-05",
    },
    "additionalneeds": "Breakfast",
}

UPDATED_VALID_B_INFO = {
    "firstname": "Updated",
    "lastname": "Person",
    "totalprice": 999,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2027-01-01",
        "checkout": "2027-01-10",
    },
    "additionalneeds": "Late checkout",
}

# BASIC PATCH
VALID_FIRSTNAME_JSON_PATCH = {"firstname" : UPDATED_VALID_B_INFO["firstname"]}

# INVALID DATA


INVALID_STRING_ENTRIES = [
    pytest.param(None,                  id="null"),
    pytest.param("",                    id="empty string"),
    pytest.param(14,                    id="wrong type"),
    pytest.param("   ",                 id="just whitespace"),
    pytest.param('s'*12345,             id="too long string"),
    pytest.param("<>()/;-{}\\",         id="suspicious chars"),
    pytest.param("👨‍👩‍👧",                  id="emoji"),
    pytest.param(True,                  id="boolean"),
    pytest.param(["a", "b"],            id="list"),
    pytest.param({"nested": "object"},  id="dict"),
]