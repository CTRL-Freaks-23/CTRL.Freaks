from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    weight = db.Column(db.Float, nullable=True)

    #initiate user
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)
        self.weight = None

    #return user data
    def get_json(self):
          return {
                    'id': self.id,
                    'username': self.username,
                    'email': self.email
                }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
          return f'<User {self.id}: {self.username}>'



#User progress for chosen workout
class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id =  db.Column(db.Integer, db.ForeignKey('excercise.id'), nullable=False)
    exercise_name = db.Column(db.String(255), db.ForeignKey('excercise.name'), nullable=False)
    progress_value = db.Column(db.Integer, default=0)

    def __init__(self, user_id, exercise_id,  exercise_name, progress_value=0):
        self.user_id = user_id
        self.progress_value = progress_value

    def __repr__(self):
        return f"<UserProgress {self.user_id} - {self.progress_value}>"
    
    def get_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'exercise_id': self.exercise_id,
            'exercise_name': self.exercise_name,
            'progress_value': self.progress_value
        }

#all Ecercises
class Exercise(db.Model):  
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(120), nullable=True)
    duration = db.Column(db.Interger, nullable=(True))

    def get_json(self):
        return {
                'exercise_id': self.id,
                'name': self.name,
                'description': self.description,
                'category': self.category,
                'duration':self.duration
               }
    
    

