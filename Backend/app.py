from flask import Flask,request,jsonify
from flask_cors import CORS
from user import *
from login import *


app = Flask(__name__)
CORS(app)

@app.route("/login",methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    return login(username,password)
    
@app.route("/signup", methods =["POST"])
def signUp():
    data = request.json
    name = data.get("name")
    username = data.get("username")
    password = data.get("password")
    age = data.get("age")
    weight = data.get("weight")
    height = data.get("height")
    goals = data.get("goals")
    
    return signUp(username,name,password,weight,height,age,goals)

@app.route("/addgoal", methods =["POST"])
def add_daily():
    data = request.json
    goal = data.get("goal")
    user_id = data.get("user_id")
    print(goal,user_id)
    add_fit_goal(user_id,goal)
    return jsonify({"message":"successful!"})


if __name__ == "__main__":
    app.run(debug=True)
