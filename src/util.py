from flask import render_template

def do_the_login():
     return render_template('post.html')

def show_the_login_from():
    return render_template('login.html')
    