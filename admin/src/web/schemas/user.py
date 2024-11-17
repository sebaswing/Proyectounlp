from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email= fields.Str(required=True)
    inserted_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

User_schema = UserSchema()