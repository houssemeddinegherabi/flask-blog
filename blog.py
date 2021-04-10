from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '68a2c99120b7e9558c126213b6989f1d'

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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


if __name__ == '__main__':
    app.run(debug=True)
