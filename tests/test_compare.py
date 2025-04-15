import requests
from deepdiff import DeepDiff

def test_compare_responses():
    payload = {"example": "data"}

    ref = requests.post("http://webtours.load-test.ru:1080/cgi-bin/nav.pl?in=home", json=payload)
    target = requests.post("http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home", json=payload)

    diff = DeepDiff(ref.json(), target.json(), ignore_order=True)
    assert diff == {}, f"Found difference: {diff}"