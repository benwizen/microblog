from flask import request
from app import app, babel


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return 'es'
