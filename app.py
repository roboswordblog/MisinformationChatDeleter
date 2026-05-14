from flask import Flask, render_template, jsonify, request, session
from dataManagment import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sendMessage")
def sendMessage():
    data = request.get_json()
    post = data.get("message")


@app.route('/getChat', methods=['POST'])
def get_chat():
    data = request.get_json()

    username = data.get("username")
    code = data.get("code")

    a = getChat(code)

    return jsonify({
        "error": a,
        "messages": a
    })


if __name__ == "__main__":
    app.run(debug=True)
