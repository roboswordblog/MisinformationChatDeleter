from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/sendMessage")
def sendMessage():
  pass

@app.route("/getChat")
def getChat():
  return {}

if __name__ == "__main__":
  app.run(debug=True)
