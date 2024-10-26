from dataclasses import dataclass
from flask import render_template

@dataclass
class Error:
        code:int
        message:str
        description:str


def error_not_found(e):
        error=Error(404,"Not Found","the requested URL was not found on the server")
#        error={
 #           "code":404,
  #          "message":"Not Found",
   #         "description":"the requested URL was not found on the server"
   #     }
        return render_template('error.html',error=error), 404

def unauthorized(e):
        error=Error(401,"Unauthorized","You are not authoried to acces this page.")

        return render_template('error.html',error=error), 401

def Forbidden(e):
        error=Error(403,"Forbidden","You are not Allowed to acces this page.")

        return render_template('error.html',error=error), 403