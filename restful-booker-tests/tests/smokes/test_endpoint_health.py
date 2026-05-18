import helpers as h
import test_data as d
import pytest


# ENDPOINT CONNECTIVITY
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