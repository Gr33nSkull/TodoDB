from trnslate import Translate
import json
from flask import Flask, request
# , jsonify

translator = Translate()

app = Flask(__name__)

@app.route('/<query>')
def index(query):

    if len(query) < 3:
        return 411

    #Gives Token
    if query == "ping":
        return translator.ping(), 200


# TODO NAREDI UPDATE
    elif query == "update_ls":
        with open("server_ls.txt", "r") as v:
            a = json.load(v)

        return json.dumps(a)

    elif query == "update_tsk":
        with open("server_tsk.txt", "r") as v:
            a = json.load(v)

        return json.dumps(a)

    # checks if it wants to edit tasks
    elif query[0] + query[1] + query[2] == "tsk":
        return translator.tsk(query), 200
    # checks if it wants to edit lists
    elif query[0] + query[1] == "ls":
        return translator.ls(query), 200

    else:
        return "INVALID REQUEST", 400
