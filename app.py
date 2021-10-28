from flask import Flask
from flask import request, jsonify, make_response
import os
from liwc import Liwc
import calculation

app = Flask(__name__)

LIWC_FILEPATH_EN = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'dict/LIWC2015_English_Flat.dic'))

LIWC_FILEPATH_ES = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'dict/LIWC2007_Spanish_Flat.dic'))

liwc_en = Liwc(LIWC_FILEPATH_EN)
liwc_es = Liwc(LIWC_FILEPATH_ES)


@app.route('/health/ready')
def ready():
    return 'ok'


@app.route('/health/life')
def life():
    return 'ok'


@app.route('/')
def index():
    content = """ I hope your morning is as radiant as your amazing smile.
#2: May this new morning bring forth miracles and blessings. I cherish and adore you.
#3: The long night is gone, and the morning has come. It is time to give me some hugs and kisses.
#4: Wake up with a smile darling, because you are strong, smart, energetic and blessed.
"""

    tokens_enum = calculation.tokenize(content)
    tokens = list(tokens_enum)

    l = len(tokens)

    result = liwc_en.parse(tokens)

    return {
        'info': {
            'clout': calculation.calcClout(result, l),
            'analytics': calculation.calcAnalytic(result, l),
            'authentic': calculation.calcAuthentic(result, l),
            'tone': calculation.calcTone(result, l)
        }
    }


@app.route('/process', methods=['POST'])
def process():
    """
    process input text by the liwc method
    """
    content: str
    lang = request.args.get('lang') or 'en'

    if 'application/json' in request.content_type:
        json = request.json
        content = json['text']
        
        lang =  json['lang'] if 'lang' in json else lang

    elif 'text/plain' in request.content_type:
        content = request.get_data(as_text=True)

    else:
        return make_response("Unsupported media type",415)


    tokens_enum = calculation.tokenize(content)
    tokens = list(tokens_enum)

    l = len(tokens)

    liwc =  liwc_en if lang=='en' else liwc_es

    result = liwc.parse(tokens)

    return {
        'classification': result,
        'info': {
            'clout': calculation.calcClout(result, l),
            'analytics': calculation.calcAnalytic(result, l),
            'authentic': calculation.calcAuthentic(result, l),
            'tone': calculation.calcTone(result, l)
        },
        'meta': {
            'lang': lang
        }
    }


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()
