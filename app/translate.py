import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Content-Type': 'application/json'
    }
    body = [{
        'text': text
    }]
    r = requests.post(f'{current_app.config["MS_TRANSLATOR_ENDPOINT"]}&from={source_language}&to={dest_language}',
                      headers=auth, json=body)

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
