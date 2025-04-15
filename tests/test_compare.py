import requests
from deepdiff import DeepDiff

def test_compare_responses():
    payload = {"example": "data"}

    ref = requests.get("http://webtours.load-test.ru:1080/cgi-bin/nav.pl?in=home")
    target = requests.get("http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home")

    assert ref.status_code == 200, f"Reference API returned {ref.status_code}"
    assert target.status_code == 200, f"Target API returned {target.status_code}"

    try:
        ref_json = ref.json()
        target_json = target.json()
    except ValueError:
        print("One of the responses is not in JSON format.")
        print("Reference response:")
        print(ref.text[:300])
        print("Target response:")
        print(target.text[:300])
        assert False, "Invalid JSON in one of the responses"

    diff = DeepDiff(ref_json, target_json, ignore_order=True)
    assert diff == {}, f"Found difference: {diff}"