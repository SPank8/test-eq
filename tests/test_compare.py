import requests
from deepdiff import DeepDiff

def test_compare_responses():
    payload = {"example": "data"}

    ref = requests.post("https://reference-api.example.com/endpoint", json=payload)
    target = requests.post("https://target-api.example.com/endpoint", json=payload)

    diff = DeepDiff(ref.json(), target.json(), ignore_order=True)
    assert diff == {}, f"Found difference: {diff}"