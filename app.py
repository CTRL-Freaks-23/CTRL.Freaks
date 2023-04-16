from flask import Flask, render_template, request

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")



@app.route("/workout")
def workout():
    return render_template("workout.html")



@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/remix")
def remix():
    return render_template("remix.html")



@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    # save name and email to database
    return render_template("signup.html", name=name, email=email)


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
