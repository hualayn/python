from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'hello.world'
# from flask_script_demo.models import Users
# db.drop_all()
# db.create_all()
