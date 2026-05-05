"""Shared fixtures for the Restful-Booker test suite."""

import httpx
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def client() :
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        yield client