from marshmallow import Schema, fields

class EmailSchema(Schema):
    email = fields.Email(required=True)
    app_id = fields.String(required=True)
    ip = fields.String()
    reason = fields.String()
    date_created = fields.DateTime()
    