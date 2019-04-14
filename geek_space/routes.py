from geek_space import app
from flask import Response, render_template
from geek_space.forms import RegistrationForm, LoginForm


@app.route('/')
def home():
    return render_template('home.html', status=200)


@app.route('/workspace')
def workspace():
    return render_template('workspace.html', status=200)


@app.route('/test')
def test():
    return Response('OK', status=200)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
