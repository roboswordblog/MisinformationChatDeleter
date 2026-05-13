from flask import Flask, render_template, jsonify, request
from dataManagment import *
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/sendMessage")
def sendMessage():
  pass

@app.route("/getChat")
def getChat():

  webData = request.get_json()
  stuff = getChat(webData["code"])
  data = {"error":stuff != False,"chatMessages":stuff}

  return data

if __name__ == "__main__":
  app.run(debug=True)
