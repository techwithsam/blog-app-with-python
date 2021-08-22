from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
home = "views.home";

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Welcome back!', category='success')
                login_user(user, remember=True)
                return redirect(url_for(home))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not correct', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        email_exist = User.query.filter_by(email=email).first()
        username_exist = User.query.filter_by(username=username).first()

        if email_exist:
            flash('Email already exist', category='error')
        elif username_exist:
            flash('Username already exist', category='error')
        elif password1 != password2:
            flash('Password not match', category='error')
        elif len(username) < 2:
            flash('Username too short', category='error')
        elif len(password1) < 6:
            flash('Password too short', category='error')
        elif len(email) < 4:
            flash('Email is invalid', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Sign up successfully', category='success')
            return redirect(url_for(home))
        
    return render_template('sign-up.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(home))
    