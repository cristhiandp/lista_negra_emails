from marshmallow import Schema, fields

class EmailSchema(Schema):
    email = fields.Email(required=True)
    app_uuid = fields.String(required=True)
    ip = fields.String()
    blocked_reason = fields.String()
    date_created = fields.DateTime()
    