from geek_space import app, bcrypt, db
from geek_space.utils.file import save_picture
from flask import Response, render_template, flash, redirect, url_for, request
from geek_space.forms.user import RegistrationForm, LoginForm, ProfileForm
from geek_space.models.user import User
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def home():
    return render_template('home.html', status=200)


@login_required
@app.route('/workspace')
def workspace():
    return render_template('workspace.html', status=200)


@login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    image_file = url_for('static', filename=f'img/profile_pics/{current_user.image_file}')
    form = ProfileForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_picture(form.image.data)
            current_user.image_file = image_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your account has been updated', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)


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
    return render_template('register.html', title='Register', form=form)


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
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    redirect(url_for('home'))


@app.route('/note/new')
@login_required
def new_note():
    return render_template('create_note.html', title='Note')
