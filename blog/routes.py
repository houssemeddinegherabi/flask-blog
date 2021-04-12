from flask import render_template, url_for, flash, redirect, request
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [{
    'author': 'John Doe',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 21, 2018'
}, {
    'author': 'Mr. X',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 10, 2018'
}]


@app.route('/')
def home():
    return render_template('home.html', posts=posts, title="Home")
    # You can also write multiline html by using ''' </> '''


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register_method():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. You can now login!', 'success')
        return redirect(url_for('login_method'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_method():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(
                url_for('home'))
        else:
            flash('Invalid Login. Please check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route("/logout")
def logout_method():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')