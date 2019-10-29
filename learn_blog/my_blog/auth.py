from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import g, session
from werkzeug.security import generate_password_hash, check_password_hash

from my_blog.db import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/')
def auth_redirect():
    return redirect(url_for('auth.login'))

# 在每次向服务器请求（网页）时，执行load_login_user，判断是否存在用户信息，如果存在则将这个信息存在全局变量g内供网页显示
@bp.before_app_request
def load_login_user():
    user_id = session.get("login_user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()

def have_user(username):
    user = User.query.filter_by(name=username).first()
    if user:
        return user

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        user = have_user(username)
        error = None

        if user is None:
            error = '没有该用户！'
        elif not check_password_hash(user.password, password):
            error = '密码不正确！'

        if error is None:
            session.clear()
            session["login_user_id"] = user.id
            return redirect(url_for('blog.index'))

        return error

    else:
        return render_template('auth/login.html')

@bp.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        error = None

        if not username:
            error = '必须填写用户名'

        elif not password:
            error = '必须填写密码'

        elif  password != password2:
            error = '密码不一致'

        else:

            if have_user(username):
                error = '已存在用户'

            else:
                try:
                    new_user = User(name=username, password=generate_password_hash(password))
                    db.session.add(new_user)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                # print(search_user(username))
                # return '注册成功'
                return redirect(url_for('auth.login'))

        return error

    return render_template('auth/register.html')

@bp.route('/logout/', methods=('GET', 'POST'))
def log_out():
    session.clear()
    return redirect(url_for('blog.index'))