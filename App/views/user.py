from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    create_exercise,
    shuffle_exercise,
    get_exercise,
    get_all_exercise_json,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


@user_views.route('/templates/profile', methods=['GET'])
def get_user_profile_page():
    @login_required
    user= User.query.filter_by(username=current_user.username).first()
	return render_template('profile.html', username=user.username, email=user.email)


@user_views.route('/workout', methods=['GET'])
@user_views.route('/workout/<int:exercise_id>', methods=['GET'])
@login_required
def workout_page():
  exercises = Exercise.query.all()
  return render_template('workout.html', exercises=exercises)

@user_views.route('/remix', methods=['GET'])
@login_required
def get_remix():
    exercises= Exercise.query.all()
    return render_template('remix.html', exercises=exercises)




