from App.models import User, UserProgress, Exercise
from App.database import db
import random

#user functions
def create_user(username, email, password, weight):
    try:
        newuser = User(username=username,email=email, password=password, weight=weight)
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        # user.password = selfpassword
        # user.email =email
        # user.weight = weight
        db.session.add(user)
        return db.session.commit()
    return None
    
#user progress functions
def update_progress(id, exercise_id, exercise_name, progress_value):
    user = get_user(id)
        
    if(user):
        progress_value = progress_value
        #exercise_name = exercise_name
        db.session.add(progress_value)
        db.session.commit()
        return progress_value
    return False


#exercise functions
def create_exercise(name, description, category, duration):
    try: 
        exercise= Exercise(name=name, description=description, category=category, duration=duration)
        db.seesion.add(exercise)
        db.session.commit()
        return exercise
    except:
        return None

def shuffle_exercise(category):
    try:
        workouts = Exercise.query.filter_by(category=category).first()
        #for 3 in workouts:
        w1= random.shuffle(workouts)
        w2= random.shuffle(workouts)
        w3= random.shuffle(workouts)
        return w1, w2, w3
    except:
        return None
    
def get_exercise(id):
    return Exercise.query.get(id)

def get_all_exercise_json():
    exercises = Exercise.query.all()
    if not exercises:
        return []
    exercise = [exercise.get_json() for exercise in exercises]
    return exercise
    