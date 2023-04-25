from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import login_required, login_user, current_user, logout_user
from App.models import db
from App.models import User, Exercise, UserProgress
from App.controllers import create_user, create_exercise

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
@index_views.route('/login', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bob@bob.com', 'bobpass', '120')
    create_user('jon', 'jon@jmail.com', 'jonpass', '')
    create_exercise('Knees Up Ab Crunch', '', 'core', '40')
    create_exercise('Bent Leg Raises', '', 'core', '40')
    create_exercise('Parallel Stance Squat', '', 'lower', '40')
    create_exercise('Side to Side Jab With Rotation', '', 'core', '20')
    create_exercise('Flutter Kicks', '', 'lower', '20')
    create_exercise('PushUps', '', 'upper', '40')
    create_exercise('Plank Push Up', '', 'upper', '40')
    create_exercise('Hand Release Push Up', '', 'upper', '40')    
    return jsonify(message='db initialized!')


@index_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})