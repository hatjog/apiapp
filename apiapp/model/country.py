from marshmallow import post_load
import pymssql
import sys
from flask import jsonify

from .region import Region, RegionSchema
from .region_type import RegionType


class Country(Region):
    __conn: pymssql._pymssql
    __cursor: pymssql.Cursor

    def __init__(self, id=None, name=None):
        super(Country, self).__init__(id, name, RegionType.COUNTRY)
        self.__conn = pymssql.connect(server='localhost\\SQLEXPRESS', user='user', password='user', database='apiapp')
        self.__cursor = self.__conn.cursor()

    def __repr__(self):
        return '<Country(name={self.name!r})>'.format(self=self)

    def list(self):
        self.__cursor.execute('SELECT c.ID, c.Name FROM country AS c order by ID;')
        row = self.__cursor.fetchone()
        while row:
            yield [row[0], str(row[1])]
            row = self.__cursor.fetchone()

    def to_json(self):
        country_list = []
        countryName: str
        for (countryID, countryName) in self.list():
            country_list.append({'id': countryID, 'name': countryName})
        return jsonify(country_list)

    def add(self, record):
        if record is None:
            print('Error in adding country to the database: no country', file=sys.stderr)
            exitcode = 500
            exit_description = 'Error in adding country to the database: no country'
        else:
            statement = "INSERT INTO country (name) VALUES ('" + record.get("name") + "');"
            exitcode = 0
            exit_description = 'New Country added to the database: %s' % (record.get("name"))
            try:
                self.__cursor.execute(statement)
                self.__conn.commit()
            except pymssql.Error as e:
                exitcode = 500
                exit_description = 'MSSQL Error in provided data'
                print('Error in adding country to the database: %d: %s' % (e.args[0], e.args[1]), file=sys.stderr)
            else:
                print('New Country added to the database: %s' % (record.get("name")), file=sys.stderr)

        return exitcode, exit_description

    def save(self):
        statement = "INSERT INTO country (name) VALUES ('" + self.name + "');"
        exitcode = 0
        exit_description = ''
        try:
            self.__cursor.execute(statement)
            self.__conn.commit()
        except pymssql.Error as e:
            exitcode = 500
            exit_description = 'Error in provided data'
            print('Error in adding country to the database: %d: %s' % (e.args[0], e.args[1]), file=sys.stderr)
        else:
            print('New Country added to the database: %s' % (self.name), file=sys.stderr)
        return exitcode, exit_description

    def delete(self, record):
        if record is None:
            exitcode = 500
            exit_description = 'Error in deleting country from the database: no country'
        else:
            statement = "DELETE FROM country WHERE name = '" + record.get("name") + "';"
            exitcode = 0
            exit_description = 'Deleted from country: ' + record.get("name")
            try:
                self.__cursor.execute(statement)
                self.__conn.commit()
            except pymssql.Error as e:
                exitcode = 500
                exit_description = 'MSSQL Error in provided data'
                print('Error in deleting country: %d: %s' % (e.args[0], e.args[1]), file=sys.stderr)
        return exitcode, exit_description


class CountrySchema(RegionSchema):
    def __init__(self):
        RegionSchema.__init__(self)

    @post_load
    def make_country(self, data, **kwargs):
        return Country(data)





# 0.0.1
