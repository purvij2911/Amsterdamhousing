import json
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_get_woz_value():
    with app.test_client() as client:
        response = client.get('/api/get_woz_value?parameter1=test&parameter2=1.0&parameter3=2.0&parameter4=3.0&parameter5=4.0&parameter6=5.0&parameter7=6.0&parameter8=7.0&parameter9=8.0')
        assert response.status_code == 200
        assert isinstance(response.json['woz_value'], (int, float))




