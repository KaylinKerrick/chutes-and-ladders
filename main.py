from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
  session["turns"] = 10  #each user will start on space 1 with 10 turns when the page loads
  session["space"] = 1
  return render_template("index.html", turns = session["turns"], space = session["space"], submitted = False) #submitted = false is so the "you rolled a ____" message does not appear yet

@app.route('/click', methods = ["POST", "GET"])
def rollDice(): 
  if "dice" in request.form: #this will run once the dice is clicked
    dice = random.randint(1,6) #rolls a random number between 1 and 6
    session["space"] += dice #every roll is added to the space they're on
    session["turns"] += -1 #every roll is using up one of the ten turns
    if session["space"] == 11:  #chute on space 11 and 2
      session["space"] = 2
    elif session["space"] == 12:  #ladder on space 12 and 16
      session["space"] = 16
    elif session["space"] == 18:  #ladder on space 18 and 24
      session["space"] = 24
    elif session["space"] == 19: #chute on space 19 and 8
      session["space"] = 8
    elif session["space"] == 26: #chute on space 26 and 15
      session["space"] = 15
    return render_template("index.html", dice=dice, turns = session["turns"], space = session["space"], submitted = True) #submitted = true so the "you rolled a ___" message will appear
  elif "reset" in request.form: #this will run once the reset button is pushed
    session["space"] = 1   #reseting the space to 1 and the # of turns to 10
    session["turns"] = 10
    return render_template("index.html", turns = session["turns"], space = session["space"], submitted = False)
  return render_template("index.html", turns=session["turns"], space=session["space"], submitted=False)


app.run(host='0.0.0.0', port=81)


  

  