import pytest
import requests
import json

url = "http://127.0.0.1:5000/person/"

person_dict = {
    "1": "Иванов Сергей Иванович",
    "2": "Петров Николай Семенович"
}

testdata = [pytest.param("1", 200, person_dict["1"], persomarks=pytest.mark.basic),
            pytest.param("2", 200, person_dict["2"], marks=pytest.mark.basic),
            pytest.param("3", 404, "Смирнов Иван Петрович", marks=[pytest.mark.basic, pytest.mark.xfail])]

# testdata = [("1", 200, person_dict["1"]),
#             ("2", 200, person_dict["2"]),
#             ("3", 404, "Смирнов Иван Петрович")]

@pytest.mark.parametrize("person_id,resp_code,expected", testdata)
def test_service(person_id, resp_code, expected):
    resp = requests.get(url + person_id)
    assert resp.status_code == resp_code
    if resp_code == 200:
        name = json.loads(resp.text)
        print(resp.text)
        assert name['ФИО'] == expected

#with pytest.raises(json.decoder.JSONDecodeError):
