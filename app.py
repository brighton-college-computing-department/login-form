from flask import Flask, request, render_template

app = Flask(__name__)


def valid_login(username, password):
    return True


def log_the_user_in(username):
    return render_template('profile.html', username=username)


@app.route("/")
def main_page():
    return "This is the main page, it does NTHING"


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)
