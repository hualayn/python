from flask_script_demo import db
from flask_script_demo.models import Users

new_user = Users(name='test',email='test_email')
db.session.add(new_user)
db.session.commit()

# import os
# from flask_script_demo import app
# DATABASE=os.path.join(app.instance_path, "db.database")
# print(DATABASE)
# print(app.instance_path)