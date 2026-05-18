import test_data as d
import pytest

# --- CRUD HELPERS
def create_booking(client, booking_info=d.DEFAULT_VALID_B_INFO) :
    response = client.post("/booking", json=booking_info)
    return response

def find_booking(client, b_id) :
    response = client.get(f"/booking/{b_id}")
    return response

def find_booking_id(response):
    return response.json()["bookingid"]

def delete_booking(client, b_id):
    response = client.delete(
        f"/booking/{b_id}",
    )
    return response

def put_booking(client, b_id, b_data=d.UPDATED_VALID_B_INFO):
    response = client.put(
        f"/booking/{b_id}",
        json=b_data,
    )
    return response

def patch_booking(client, b_id, patch_data_dict):
    response = client.patch(
        f"/booking/{b_id}",
        json=patch_data_dict,
    )
    return response

# --- TEST SETUP HELPERS
def with_known_bugs(cases, bug_map):
    """Add xfail marks to specific case IDs.

    Args:
        cases: list of pytest.param objects
        bug_map: dict mapping case_id -> reason string

    Returns:
        new list with xfail marks applied where matched
    """
    result = []
    for case in cases:
        case_id = case.id
        if case_id in bug_map:
            new_marks = list(case.marks) + [pytest.mark.xfail(reason=bug_map[case_id])]
            result.append(pytest.param(*case.values, id=case_id, marks=new_marks))
        else:
            result.append(case)
    return result