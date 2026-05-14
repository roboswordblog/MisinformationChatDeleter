from flask import Flask, render_template, jsonify, request, session
from dataManagment import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sendMessage", methods=["POST"])
def sendMessage():
    data = request.get_json()
    post = data.get("message")
    username = data.get("username")
    return jsonify({"message": post})

@app.route("/getAllMessages", methods=["GET", "POST"])
def getAllMessages():
    return jsonify({"messages": getAllChatMessages(request.get_json().get("code"))})


@app.route('/getChat', methods=['POST'])
def get_chat():
    data = request.get_json()

    code = data.get("code")

    a = getChat(code)

    return jsonify({
        "error": a,
        "messages": a
    })


if __name__ == "__main__":
    app.run(debug=True)
