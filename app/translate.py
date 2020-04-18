import json
import requests
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Content-Type': 'application/json'
    }
    body = [{
        'text': text
    }]
    r = requests.post(f'{app.config["MS_TRANSLATOR_ENDPOINT"]}&from={source_language}&to={dest_language}',
                      headers=auth, json=body)

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
