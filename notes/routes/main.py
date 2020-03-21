from flask import Response, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user

from geek_space import app, bcrypt, db
from geek_space.forms.user import RegistrationForm, LoginForm
from geek_space.models.user import User


# TODO refactor all app to use blueprints and split to modules
# link: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure

@app.route('/')
def home():
    return render_template('home.html', status=200)


@app.route('/test')
def test():
    return Response('OK', status=200)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account is been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('auth/login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
