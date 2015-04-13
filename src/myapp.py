# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, redirect, url_for, g
from  db import mysql_db

app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_url = request.form.get('image_url')
        return render_template('index.html', image_url = image_url)
    else:
        username = session['username'] if 'username' in session else ''
        sql = "SELECT * FROM wp_posts where post_status='publish'"
        result = mysql_db.execute(sql).fetchall()
        data = ()
        for line in result[::-1]:
            data += (line[0], line[2], line[4], line[5]),
        return render_template('index.html',
            title = 'index',
            username = username,
            data = data)

@app.route('/image')
def image():
    username = session['username'] if 'username' in session else ''
    return render_template('image.html',
        title = 'image',
        username = username)

@app.route('/review/p=<int:post_id>')
def review(post_id):
    username = session['username'] if 'username' in session else ''
    sql = "SELECT * FROM wp_posts where ID=%s" % post_id
    result = mysql_db.execute(sql).fetchall()
    data = (result[0][0], result[0][2], result[0][4], result[0][5])
    return render_template('view.html',
        title = data[3],
        username = username,
        data = data)

@app.route('/about')
def about():
    username = session['username'] if 'username' in session else ''
    return render_template('about.html',
        title = 'about',
        username = username)

@app.route('/user/<username>')
def show_user(username):
    if username not in  session:
        return redirect(url_for('login'))
    return render_template('user.html',
        title = username,
        username = username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('loginuser')
        password = request.form.get('passwd')
        if username == 'hidaen' and password == 'hidaen.com':
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', 
                title = 'login',
                username='', text="Login Fail !")
    else:
        return render_template('login.html',
            title = 'login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html',
        error = error)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html',
        error = error)

app.secret_key = "\xa2\x82\xdb\xaeP'\xc9$\xe2(\xf1\x18S\x81\x1d\x1bld'\x9bny\xe7!"

if __name__ == '__main__':
    app.run(debug=True)
