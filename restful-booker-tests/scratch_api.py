"""Throwaway script to verify httpx works against Restful-Booker."""
import httpx

BASE_URL = "https://restful-booker.herokuapp.com"

# # 1. Health check
# print("=== Health check ===")
# response = httpx.get(f"{BASE_URL}/ping")
# print(f"Status: {response.status_code}")
# print(f"Body: {response.text!r}")

# 2. List all bookings
print("\n=== List bookings ===")
response = httpx.get(f"{BASE_URL}/booking")
print(f"Status: {response.status_code}")
booking_ids = response.json()
print(f"Got {len(booking_ids)} bookings; first 3: {booking_ids[:3]}")

# 3. Get one booking
first_id = booking_ids[0]["bookingid"]
print(f"\n=== Get booking {first_id} ===")
response = httpx.get(f"{BASE_URL}/booking/{first_id}")
print(f"Status: {response.status_code}")
print(f"Body: {response.json()}")

# 4. Create a new booking (no auth needed for this endpoint)
print("\n=== Create booking ===")
new_booking = {
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
response = httpx.post(f"{BASE_URL}/booking", json=new_booking)
print(f"Status: {response.status_code}")
print(f"Body: {response.json()}")