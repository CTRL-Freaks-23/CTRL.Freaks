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


@app.route("/", methods =['GET'])
def login_page():
    return render_template("login.html")

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    # save name and email to database
    return render_template("signup.html", name=name, email=email, password=password)


@app.route('/login', methods=['POST'])
def login_user_view():
  data = request.json

  user = User.query.filter_by(username = data['username']).first()
  if not user or not user.check_password(data['password']):
    return jsonify(error='bad username/password given'), 401
  else:
    return jsonify(access_token= create_access_token(identity=data['username']))


@app.route("/workout")
def workout():
    return render_template("workout.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/remix")
def remix():
    return render_template("remix.html")


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
