from flask import request

from apiapp import app

from apiapp.model.country import Country, CountrySchema
from apiapp.model.region_type import RegionType


@app.route("/countrylist")
def tablelist() -> str:
    country = Country()
    page = '<html><body>'
    page += '<h1>List of countries </h1>'
    for (countryID, countryName) in country.list():
        page += f'<p>{countryID} {countryName}</p>'
    page += '</body></html>'
    return page


@app.route("/api/v1.0/country", methods=['GET'])
def get_country():
    country = Country()
    return country.to_json()


@app.route('/api/v1.0/country/add', methods=['POST'])
def add_country():
    req = request.get_json()
    # country_data = CountrySchema().load(req)
    (exitcode, exit_description) = Country().add(req)
    if exitcode == 0:
        return exit_description, 200
    else:
        return exit_description, 600


@app.route('/api/v1.0/country/add2', methods=['POST'])
def add_country2():
    req = request.get_json()
    country = CountrySchema().load(req)
    (exitcode, exit_description) = Country().save
    if exitcode == 0:
        return exit_description, 200
    else:
        return exit_description, 600


@app.route('/api/v1.0/country/delete', methods=['POST'])
def delete_country():
    req = request.get_json()
    (exitcode, exit_description) = Country().delete(req)
    if exitcode == 0:
        return exit_description, 200
    else:
        return exit_description, 600

