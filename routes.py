from flask import Flask, request, jsonify
from flask_cors import CORS
from main import custumer
from main import registerTicket, deleteTicket

app = Flask("JETickets")
CORS(app)

@app.route("/api/tickets", methods=["GET"])
def getDataTicket():
    tickets = []
    for i in custumer.find():
        tickets.append(i)
    return jsonify({"tickets": tickets})

@app.route("/api/tickets", methods=["POST"])
def postDataTicket():
    body = request.get_json()

    if "title" not in body:
        return response(400, "parameter title required")
    elif "category" not in body:
        return response(400, "parameter category required")
    elif "description" not in body:
        return response(400, "parameter description required")
    elif "amount" not in body:
        return response(400, "parameter amount required")
    elif "date" not in body:
        return response(400, "parameter date required")
    elif "time" not in body:
        return response(400, "parameter time required")

    ticket = registerTicket(body["title"], 
        body["category"], 
        body["description"], 
        body["amount"], 
        body["date"],
        body["time"])
    
    return response(200, "published successfully", "ticket" , ticket)

@app.route("/api/tickets/<id>", methods=["DELETE"])
def deleteDataTicket(id):
    deleteTicket(int(id))
    return response(200, f"successfully deleted")

def response(status, message, name_content = False, content = False):
    response = {}
    response["status"] = status
    response["message"] = message

    if name_content and content:
        response[name_content] = content

    return response

app.run('0.0.0.0', port=3001)