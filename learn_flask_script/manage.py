from flask_script_demo import app, db
from flask_script_demo.models import Users
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

@manager.command
def greet():
    print('hello,world')

@manager.command
def create_table():
    db.drop_all()
    db.create_all()

@manager.command
def add_user():
    new_user = Users(name='test_name', email='test_email')
    db.session.add(new_user)
    db.session.commit()

@manager.option('-u', '--username', dest='username')
@manager.option('-e', '--email', dest='email')
def add_user_(username, email):
    new_user = Users(name=username, email=email)
    db.session.add(new_user)
    db.session.commit()

Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()