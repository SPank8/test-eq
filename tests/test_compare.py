import requests
import allure

@allure.title("Сравнение HTML-ответов с двух серверов")
@allure.description("Проверяем, что страницы REF и TARGET возвращают одинаковый HTML и статус код 200.")

def test_compare_html_responses():
    url_ref = "http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home"
    
    url_target = "http://webtours.load-test.ru:1090/cgi-bin/nav.pl?in=home"

    with allure.step(f"GET запрос к REF: {url_ref}"):
        ref = requests.get(url_ref)
        allure.attach(ref.text, name="REF Response (полный)", attachment_type=allure.attachment_type.TEXT)
        assert ref.status_code == 200, f"REF вернул {ref.status_code}"

    with allure.step(f"GET запрос к TARGET: {url_target}"):
        target = requests.get(url_target)
        allure.attach(target.text, name="TARGET Response (полный)", attachment_type=allure.attachment_type.TEXT)
        assert target.status_code == 200, f"TARGET вернул {target.status_code}"

    with allure.step("Сравнение HTML содержимого"):
        if ref.text != target.text:
            allure.attach(ref.text, name="REF (diff)", attachment_type=allure.attachment_type.TEXT)
            allure.attach(target.text, name="TARGET (diff)", attachment_type=allure.attachment_type.TEXT)
        assert ref.text == target.text, "HTML ответы отличаются!"
        
        