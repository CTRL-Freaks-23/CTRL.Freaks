from App.database import db

class Workouts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  type = db.Column(db.String(255), nullable=False)
  muscle = db.Column(db.String(255), nullable=False)
  equipment = db.Column(db.String(255), nullable=False)
  difficulty = db.Column(db.String(255), nullable=False)
  instructions = db.Column(db.String(255), nullable=False)

  def get_json(self):
   return {
     'id': self.id,
     'name': self.name,
     'type': self.type,
     'muscle': self.muscle,
     'equipment': self.equipment,
     'difficulty': self.difficulty,
     'instructions': self.instructions,
    }