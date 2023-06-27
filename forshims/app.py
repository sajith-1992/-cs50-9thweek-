from flask import Flask, render_template, request, redirect
import sqlite3
from sqlalchemy.pool import SingletonThreadPool


app = Flask(__name__)
db = sqlite3.connect("sport.db",check_same_thread=False)

c = db.cursor()              #creating db

#c.execute("""CREATE TABLE registrants(id INTEGER,name TEXT NOT NULL, sport TEXT NOT NULL,PRIMARY KEY (id))""") #create table  
#REGISTRANTS = {}
c.exicute("""ALTER TABLE registrants(
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;) """
)
SPORTS = ["soccer","batminton","basketball"]

@app.route("/")
def index ():
  return render_template("index.html" , sports= SPORTS)
@app.route("/deregister",methods=["POST"])
def deregistrant():
  id= request.form.get("id")
  print(id)
  
  if id:
     c.execute("DELETE FROM registrants WHERE id=?",id)
  return redirect("/registrant")

@app.route("/register",methods=["POST"])
def register():
  name = request.form.get("name")
  if not  name:
    return render_template("failure.html")
  sport = request.form.get("sport")
  if sport not in SPORTS:
    return render_template("failure.html")
   
  c.execute(" INSERT INTO registrants(name,sport) VALUES(?,?)", ( name,sport)) 
  db.commit()
 # REGISTRANTS[name] = sport                      
  # return  render_template("test.html")
  # return redirect('/registrant')

  return redirect("/registrant")

@app.route("/registrant")
def registrant():
    # return render_template("test.html")
    # return render_template("registrant.html")
    c.execute("SELECT *  FROM registrants")
    registrants=c.fetchall()
    
    # for row in registrants:
    #    print(row)

    return render_template("registrant.html", registrants=registrants)