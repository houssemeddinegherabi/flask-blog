from flask import render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

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
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid Username or Password!!', 'danger')
    return render_template('login.html', title="Login", form=form)
