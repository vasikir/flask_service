import pytest
import requests
import json

from requests.sessions import session

url = 'http://127.0.0.1:8888/person/'

person_dict = {
    '1': 'Иванов Сергей Иванович',
    '2': 'Петров Николай Семенович'
}

def test_positive_service():
    resp = requests.get(url + '1')
    assert resp.status_code == 200
    name = json.loads(resp.text)
    assert name['ФИО'] == person_dict['1']

def test_nonvalid_methods():
    with requests.Session() as s:
        req = requests.Request('POST', url + '1')
        prepped = req.prepare()
        resp = s.send(prepped)
        assert resp.status_code == 405

negative_testdata = ['123',' 2', '2 ', '1 2', '-1', '0',
                    '!', '?', '#', '&', '_', '/', '//',
                    'abc', 'абв', '']

@pytest.mark.parametrize('person_id', negative_testdata)
def test_negative_service(person_id):
    resp = requests.get(url + person_id)
    assert resp.status_code == 404
