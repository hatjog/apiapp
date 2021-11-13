import apiapp

import apiapp.model.region_type
import apiapp.model.country as ct
from apiapp import apiapp
import pytest

sch1 = {'id': 1, 'name': 'Poland'}

@pytest.fixture
def client():
    apiapp.app.config['TESTING'] = True

    with apiapp.app.test_client() as client:
        # with apiapp.app.app_context():
        #    apiapp.init_db()
        yield client

def test_apiapp(client):
    """Start with a simple test."""

    rv = client.get('/')
    assert b'Hello World from views!' in rv.data

def test_countrylist(client):

    rv = client.get('/countrylist')
    assert b'<p>1 Poland</p><p>2 France</p><p>3 Czech</p><p>4 Germany</p>' in rv.data


def test_add_country(client):

    rv = client.post('/api/v1.0/country/add', json={"id": 10, "name": "USA2"}, follow_redirects=True)
    assert b'Error in adding country to the database' not in rv.data
    assert b'New Country added to the database' in rv.data
    assert b'USA2' in rv.data

def test_delete_country(client):

    rv = client.post('/api/v1.0/country/delete', json={"id": 10, "name": "USA2"}, follow_redirects=True)
    assert b'Error in' not in rv.data
    assert b'Deleted from' in rv.data
    assert b'USA2' in rv.data


class TestRegionScheme:
    def test_make_region(self):
        region = ct.RegionSchema().load({'id': 1, 'name': 'Poland'})
        assert True

class TestCountryScheme:
    def test_make_country(self):
        country = ct.CountrySchema().load({'id': 1, 'name': 'Poland'})
        assert True
