from flask import Blueprint, render_template, redirect, url_for, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('sign-up.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))
    