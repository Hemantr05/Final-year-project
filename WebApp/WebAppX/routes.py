from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post



posts = [
    {
        'author': 'Shritej',
        'title': 'Twitter Data Collection',
        'content': 'Twitter Keywords',
        'date_posted': 'Jan 20, 2020'
    },
    {
        'author': 'Hemant',
        'title': 'Facebook Data Collection',
        'content': 'Facebook Keywords',
        'date_posted': 'Jan 22, 2020'
    },
    {
        'author': 'Akshay',
        'title': 'LinkedIn Data Collection',
        'content': 'LinkedIn Keywords',
        'date_posted': 'Jan 25, 2020'
    },
    {
        'author': 'Mihir',
        'title': 'Instagram Data Collection',
        'content': 'Instagram Keywords',
        'date_posted': 'Jan 27, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
