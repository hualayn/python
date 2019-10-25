import sqlite3

# 新建表
def create_table():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = '''
    create table posts(
    id integer primary key autoincrement,
    content text
    )
    '''
    cur.execute(sql)
    cur.close()
    con.close()
    print('新建表')

#删除表
def drop_table(tab):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = " drop table " + tab
    cur.execute(sql)
    cur.close()
    con.close()
    print('删除表')

# 插入数据
def insert_data(post):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = '''
    insert into posts(content)
    values
    (?)
    '''
    cur.execute(sql, (post,))
    con.commit()
    cur.close()
    con.close()
    print('插入数据')

# 查询posts
def search_post():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = '''
    select * from posts
    '''
    results = cur.execute(sql)
    results_all = results.fetchall()

    for r in results_all:
        print(r)

    cur.close()
    con.close()
    print('查询posts')

# 查询表格数据
def search_table(tab, d):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = " select * from " + tab + " where id = ? "
    results = cur.execute(sql, (d, ))
    results_all = results.fetchall()

    for r in results_all:
        print(r)

    cur.close()
    con.close()
    print('查询table')

#删除数据
def delete_data(tab, d):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = "delete from " + tab + " where id = ?"
    cur.execute(sql, (d,))
    con.commit()
    cur.close()
    con.close()
    print('删除数据')

#更新数据
def update_data(tab, content, d):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    sql = " update " + tab + " set content = ? where id = ? "
    cur.execute(sql, (content, d))
    con.commit()
    cur.close()
    con.close()
    print('修改数据')

#create_table()
#drop_table('users')
#insert_data('haha')
search_post()
#search_table('users', '1')
#delete_data('posts', '1')
#update_data('posts', 'teteteetetetete', '3')