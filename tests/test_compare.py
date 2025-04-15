import requests

def test_compare_html_responses():
    
    ref = requests.get("http://webtours.load-test.ru:1080/cgi-bin/nav.pl?in=home")
    target = requests.get("http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home")

    assert ref.status_code == 200, f"Reference returned {ref.status_code}"
    assert target.status_code == 200, f"Target returned {target.status_code}"

    # Сравниваем HTML-ответы
    assert ref.text == target.text, "HTML responses are different"