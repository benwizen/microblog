from flask import request, current_app
from app import babel


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
    # return 'es'
