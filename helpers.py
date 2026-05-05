

# CRUD helper functions
def create_booking(client, booking_info=None) :
    if booking_info is None :
        booking_info = {
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

    response = client.post("/booking", json=booking_info)
    return response

def find_booking(client, b_id) :
    response = client.get(f"/booking/{b_id}")
    return response

def find_booking_id(response):
    return response.json()["bookingid"]

def delete_booking(client, auth_token, b_id):
    response = client.delete(
        f"/booking/{b_id}",
        headers={"Cookie": f"token={auth_token}"},
    )
    return response