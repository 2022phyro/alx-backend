from flask import Flask, render_template, request, flash
from flask_babel import Babel, gettext, refresh, force_locale
app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
@app.route('/')
def hello():
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    locale = request.args.get('lang')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
