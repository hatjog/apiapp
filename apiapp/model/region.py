import datetime as dt
from marshmallow import Schema, fields


class Region:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Region(name={self.name!r})>'.format(self=self)


class RegionSchema(Schema):

    id = fields.Integer()
    name = fields.Str()
    created_at = fields.Date()
    type = fields.Str()
