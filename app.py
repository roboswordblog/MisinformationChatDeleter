from flask import Flask, render_template, jsonify, request
from dataManagment import *
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/sendMessage")
def sendMessage():
  pass

@app.route("/getChat", methods=["GET", "POST"])
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
