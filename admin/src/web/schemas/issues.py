from marshmallow import Schema, fields

class Issue_schema(Schema):
    id = fields.Int(dump_only=True)
    email= fields.Str(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str()
    user_id = fields.Int(required=True)
    inserted_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

# se puede igualmente crear un esquema distinto con otras validaciones 

issue_schema = Issue_schema()
# simple_issue_schema = Issue_schema(exclude=("description",))#excluye el campo description
# simple1_issue_schema = Issue_schema(only=("id","title","status"))#solamente se ve el id, title y status
issues_schema = Issue_schema(many=True)
create_issue_schema = Issue_schema(only=("email","title","description","user_id"))#solo se ve email, title, description y user_id