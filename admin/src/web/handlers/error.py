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
        return render_template('error.html',error=error), error.code
