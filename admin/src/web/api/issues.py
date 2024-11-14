from flask import Blueprint, Response, request
from src.core import board  
from src.web.schemas.issues import issues_schema
from src.web.schemas.issues import create_issue_schema
from flask import jsonify

bp = Blueprint("issues_api",__name__,url_prefix="/api/consultas")

@bp.get("/")
def index():

    issues=board.list_issues()
    data=issues_schema.dumps(issues)
    # print(data)

    # data=[]
    # for issue in issues:
    #     data.append(
    #         {
    #             "id": issue.id,
    #             "email": issue.email,
    #             "title": issue.title,
    #             "description": issue.description,
    #             "status": issue.status,
    #             "user_id": issue.user_id,
    #             "inserted_at": issue.inserted_at,
    #             "updated_at": issue.updated_at
    #         }
    #     )

    # return {"status": "success"}, 200
    # return {"data": data}, 200
    return jsonify(data),200
    # return make_response(data,200) cambio por el profesor


@bp.post("/")
def create():
    data=request.get_json()
    errors=create_issue_schema.validate(data)
    # new_issue=create_issue_schema.load(data)
    if errors:
        # return make_response(errors,400) cambio por el profesor
        return jsonify(errors),400
    else:
        return jsonify(data),201
        # return { },201
    
    # print(data)
    # print("Errors:",errors)
    # print(new_issue)
    
    

# def make_response(data,status): el profesor lo sacó porque no le gustó la forma en que recibía o un diccionario o un json
#     if status in[200,201]:
#         return Response(data,mimetype="application/json",status=status)
#     else:
#         # return jsonify({"errors":data}),status
#         return jsonify(data),status