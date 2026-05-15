# Restful-Booker API Test Suite

A Python test suite for the [Restful-Booker](https://restful-booker.herokuapp.com/). 

## Purpose

Practice work for my career transition from manual to automated Test Engineering. Also testing a workflow for LLM-driven tutoring (although I'm coding it by hand for learning purposes.)

## What's covered

The suite tests the following endpoints:

- **`GET /ping`** — health check
- **`GET /booking`** — list bookings
- **`GET /booking/{id}`** — retrieve a single booking
- **`POST /booking`** — create a booking (no auth required)
- **`PUT /booking/{id}`** — full replacement (auth required)
- **`PATCH /booking/{id}`** — partial update (auth required)
- **`DELETE /booking/{id}`** — deletion (auth required)
- **`POST /auth`** — token retrieval

### UPCOMING:
Plus negative testing of invalid endpoints and edge-case input handling. 

## Documented API quirks

Restful-Booker has several non-standard behaviors. Where it deviates from REST conventions, the suite documents the deviation explicitly:

- `GET /ping` returns `201 Created` (conventional health check would be `200 OK`)
- `POST /booking` returns `200 OK` on success (conventional create would be `201 Created`)
- Auth uses a `Cookie: token=...` header rather than the conventional `Authorization` header
- `DELETE` requests return `201 Created` (conventional success would be `200 OK` or `204 No Content`)

These are noted in test docstrings and, where the convention-correct value can be asserted, marked with `@pytest.mark.xfail` so the suite documents *both* the actual and expected behavior.


A few design choices worth noting:

- **Helpers don't assert.** HTTP wrappers in `helpers.py` return raw responses; assertion policy lives in fixtures and tests. This keeps helpers usable in both happy-path and error-case tests.
- **Two client fixtures:** `client_no_auth` and `client` (preauthenticated with cookies). Tests that need auth get it implicitly through the client — no `headers=...` boilerplate.
- **Two booking fixtures:** `shared_booking` (module-scoped, read-only) and `fresh_booking` (function-scoped, safe to mutate, auto-cleanup).
- **Test data lives in a separate module** to avoid circular dependencies between helpers and fixtures.

## Running the tests

Requires Python 3.13+.

```powershell
git clone https://github.com/<yourusername>/restful-booker-tests.git
cd restful-booker-tests
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest
```

Run a single test file:

```powershell
pytest test_updates.py -v
```

## Stack

- Python 3.13
- pytest 9.0 (test framework)
- httpx 0.28 (HTTP client)


## Notes

Restful-Booker is a shared sandbox API with rate limiting and an automated 10-minute reset to a default state. Tests are written to be independent of pre-existing data and clean up resources they create.