# Restful-Booker API Test Suite

Automated test suite for the [Restful-Booker](https://restful-booker.herokuapp.com/) practice API, demonstrating API testing patterns in Python with pytest and httpx.

## Stack

- Python 3.13
- pytest
- httpx
- pytest-freezer

## Running the tests

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest
```

## What's covered

_(In active development.)_

- Health check (GET /ping)
- Listing bookings (GET /booking)

## Notes

Restful-Booker is a known-buggy practice API. Some tests document bugs intentionally using xfail.
