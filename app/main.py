from flask import Flask, jsonify, request
from . import asking

response = {"answer":"","name":""}

app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify({"about":"Hello This is API Demo"})

@app.route("/query",methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        msg = request.get_json()
        query = msg["question"]
        nm = msg["name"]
        flag = msg["flag"]
        response["name"] = nm.lower().capitalize()
        
        if flag:
            response["answer"] = "Hello {}, How may I assist you?".format(response["name"])
            return jsonify(response),200
        if not flag:
            response["answer"] = asking.ask(query)
            return jsonify(response),200
    else:
        response["answer"] = "error"
        return jsonify(response),404

@app.errorhandler(404)
def not_found(error):
    response["answer"] = "error"
    return jsonify(response),404

if __name__ == "__main__":
    app.run(debug=True) 
