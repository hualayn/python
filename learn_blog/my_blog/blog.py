from flask import Blueprint
from flask import request, session
from flask import render_template, redirect, url_for

from my_blog import db
from my_blog.models import Post


bp = Blueprint('blog', __name__)

# @bp.app_errorhandler(404)蓝图中定义错误返回值，404代表返回错误代码，如果404错误则执行page_not_found(e)函数，其中参数e不可缺省

@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404

# 同上，内部服务器500错误时执行internal_error(error)函数
@bp.app_errorhandler(500)
def internal_error(e):
    return render_template('error/404.html'), 500

# 当蓝图时，不能使用errorhandler(404)钩子，只能使用全局的app_errorhandler钩子来触发函数page_not_found执行
# @bp.errorhandler(404)
# def page_not_found(error):
#     return render_template('error/404.html'), 404

@bp.route('/', methods=('GET', 'POST'))
def index():
    posts = Post.query.all()
    # login_user = session.get('login_user_id')
    # if session.get('login_user_id') is None:
    #     print('no user logged in')
    # else:
    #     user_id = session.get('login_user_id')
    #     print(user_id)

    return render_template('blog/index.html', posts=posts)

@bp.route('/write/', methods=('GET', 'POST'))
def write_article():
    if request.method == 'POST':
        author_id = session["login_user_id"]
        if author_id:
            title = request.form["title"]
            content = request.form["content"]
            try:
                new_post = Post(title=title, content=content, author_id=author_id)
                db.session.add(new_post)
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
            finally:
                return redirect(url_for('blog.index'))
    else:
        return redirect(url_for('blog.index'))