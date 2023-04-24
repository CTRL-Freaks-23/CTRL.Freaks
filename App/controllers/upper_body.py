from App.models import UpperBody
from App.database import db
from App.config import config

import requests
import json


# def create_game(title, rawgId, rating='Teen', platform='ps5', boxart='https://via.placeholder.com/300x400', genre='action'):
#     newgame = Game(title=title, rawgId=rawgId, rating=rating, platform=platform, boxart=boxart, genre=genre)
#     db.session.add(newgame)
#     db.session.commit()
#     return newgame

def create_upper_command(title, muscle_group, reps=3):
    new_workout = UpperBody(title=title, muscle_group=muscle_group, reps=reps)
    db.seesion.add(new_workout)
    db.session.commit()
    return new_workout