from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
