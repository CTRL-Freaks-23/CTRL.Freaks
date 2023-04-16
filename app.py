from collections import UserString
from flask import Flask, abort, jsonify, render_template, request

app = Flask(__name__)




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


@app.route("/workout/<int:workout_id>", methods=["GET"])
def workout(workout_id):
    pass

@app.route("/workout", methods=["POST"])
def create_workout():
    pass

@app.route("/workout/<int:workout_id>/exercise", methods=["POST"])
def create_exercise(workout_id):
    pass

@app.route("/workout/<int:workout_id>/edit")
def edit_workout(workout_id):
    pass

@app.route("/workout/<int:workout_id>/update", methods=["POST"])
def update_workout(workout_id):
    pass

@app.route("/exercise/<int:exercise_id>/edit")
def edit_exercise(exercise_id):
    pass

@app.route("/exercise/<int:exercise_id>/update", methods=["POST"])
def update_exercise(exercise_id):
    pass

@app.route("/exercise/<int:exercise_id>/delete", methods=["POST"])
def delete_exercise(exercise_id):
    pass




if __name__ == "__main__":
    app.run(debug=True)
