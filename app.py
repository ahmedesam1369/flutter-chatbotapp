from flask import Flask, jsonify, request
import time

app = Flask(__name__)
@app.route("/bot", method=["POST"])

def response():
    query = dict(request.form)['Query']
    result = query + " " + time.ctime()
    return jsonify({"response": result})


if __name__ == "__main___":
    app.run(host="0.0.0.0",)