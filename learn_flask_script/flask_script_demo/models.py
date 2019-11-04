from flask_script_demo import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(30), nullable=False)