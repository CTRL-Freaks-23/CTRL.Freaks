import os
from datetime import timedelta
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'MySecretKey'
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)
    CORS(app)
    db.init_app(app)
    app.app_context().push()
    return app

app = create_app()
jwt = JWTManager(app)  #setup flask jwt-e to work with app

#Page Routes!
#Return to Login Page
@app.route("/", methods =['GET'])
def login_page():
    return render_template("login.html")

#Return to Landing Page
@app.route("/index", methods =['GET'])
def login_page():
    return render_template("index.html")    

#Return to Sign up Page
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    # save name and email to database
    return render_template("signup.html", username=name, email=email, password=password)

#Login User
@app.route('/login', methods=['POST'])
def login_user_view():
  data = request.json

  user = User.query.filter_by(username = data['username']).first()
  if not user or not user.check_password(data['password']):
    return jsonify(error='bad username/password given'), 401
  else:
    return jsonify(access_token= create_access_token(identity=data['username']))


#Display default workouts for each category incomplete!
@app.route("/begin", methods =['GET'])
#@login_required
def home_page():
    url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"
    headers = {
        "X-RapidAPI-Key": "51b70631c8msh71a2d7138dda15cp145714jsn930bb5c2d737",
        "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
    }

    uBdata = []
    lBdata = []
    coreData = []

    uB = ['chest', 'biceps', 'triceps']
    lB = ['glutes', 'hamstrings', 'calves']
    core = ['abdominals', 'lower_back', 'middle_back']
    
    for index in uB:
        querystring = {"muscle":"uB[index]"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        uBdata.appends[response]

    for index in lB:
        querystring = {"muscle":"lB[index]"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        lBdata.appends[response]

    for index in core:
        querystring = {"muscle":"core[index]"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        coredata.appends[response]    

    return render_template('home.html', upperBody=uBdata.slice(0,3), lowerBody=lBdata.slice(0,3), core=coreData.slice(0,3))


@app.route("/workout")
def workout():
    return render_template("workout.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


#Remix Upper Body workouts
@app.route("/remix1")
#@login_required
def remixUB():
    return render_template("home.html", upperBody=result)


#Remix Lower Body workouts
@app.route("/remix2")
#@login_required
def remixLB():
    return render_template("home.html", lowerBody=result)  


#Remix Core workouts
@app.route("/remix3")
#@login_required
def remixCORE():
    return render_template("home.html", core=result)      


@app.route("/exercise/<int:exercise_id>/delete", methods=["DELETE"])
@jwt_required()
def delete_exercise(exercise_id):
    user = User.query.filter_by(username=get_jwt_identity()).first()
    wrkout = UserWorkout.query.get(id)
    
    if not wrkout or wrkout.user.username != get_jwt_identity():
        return jsonify(error=f"id {id} invalid {get_jwt_identity()}"), 401
    user.delete_exercise(id, wrkout.name)
    return jsonify(message=f"{wrkout.name} removed"), 200



if __name__ == "__main__":
    app.run(debug=True)
