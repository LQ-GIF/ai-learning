import pytest
from api_utils_2 import fetch_json
import requests

URL1 = "https://nonexistent-abcxyz.com"
URL2 = "https://httpbin.org/delay/3"
URL3 = "https://httpbin.org/status/404"
def test_domain_not_exist():
    with pytest.raises(requests.exceptions.ConnectionError):
        requests.get(URL1)

def test_url_timeout():
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(URL2, timeout=1)

def test_url_httperror():
    with pytest.raises(requests.exceptions.HTTPError):
        response = requests.get(URL3)
        response.raise_for_status()

def test_domain_not_exist_1():
    assert fetch_json(URL1) == None

def test_url_timeout_1():
    assert fetch_json(URL2, timeout=1) == None

def test_url_httperror_1():
    assert fetch_json(URL3) == None