from DB import User
def login(username,password):
    user = User.find_one({"username":username}) 
    if user:
        if password ==user["password"]:
            return {"message":"user logged in successfully"}
        else:
            return{"error":"invalid login"}
    else:
        return {"error":"error no user"}
    
def signUp(username,name,password,weight,height,age,goals):
    user = User.find_one({"username":username})
    if user:
        return {"error":"user exists"}
    else:
        User.insert_one({
            "name":name,
            "username":username,
            "weight":weight,
            "height": height,
            "password":password,
            "age":age,
            "goals":goals,
            "fitness_goals": [],
            "task":[]
            
        })

        return{"message":"user created successfully"}