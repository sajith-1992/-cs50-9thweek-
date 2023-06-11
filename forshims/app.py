from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

@app.route("/")
def index ():
  return render_template("index.html")

@app.route("/register",methods=["POST"])
def register():
  name = request.form.get("name")
  sport = request.form.get("sports")
  REGISTRANTS[name] = sport
                        

  return render_template("success.html")


@app.route("/registrant")
def registrant():
  return render_template("registrant.html", registrant= REGISTRANTS)