from marshmallow import Schema, fields

class EmailSchema(Schema):
    email = fields.Email(required=True)
    app_uuid = fields.UUID(required=True)
    ip = fields.String()
    blocked_reason = fields.String(validate=lambda s: len(s) <= 255)
    date_created = fields.DateTime()
    