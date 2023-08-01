from flask import Flask, render_template, request, flash
from flask_babel import Babel, gettext, refresh
app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'



@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app.config.from_object(Config)
@app.route('/')
def hello():
    return render_template('3-index.html')

gettext('Welcome to Holberton')
gettext('Hello world')
if __name__ == '__main__':
    app.run()
