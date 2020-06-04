from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello from maddevskilz.com'


@app.route('/api/v1/users')
def get_users():
    users = [
        {"name": "Bruce", "email": "bruce@foo.com", "favoriteLanguage": "Python (for now)"},
        {"name": "Karina", "email": "karina@foo.com", "favoriteLanguage": "Ada"},
        {"name": "Kitty", "email": "kitty@foo.com", "favoriteLanguage": "Java"},
        {"name": "Phoebe", "email": "phoebe@foo.com", "favoriteLanguage": "Z80 Assembly"}
    ]
    return jsonify(users)


if __name__ == 'main':
    app.run()

