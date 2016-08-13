'''
Team: Atom

@Author Kuldeep Singh Grewal <kuldeepbb.grewal@gmail.com>
'''

from flask import Flask, url_for
app = Flask(__name__)
from config.common import Common
import json
from urllib import urlopen


@app.route('/')
def api_domain():
    return 'Welcome'


@app.route('/sentiment')
def api_sentiment():
    '''
    Remove this in future.
    '''
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


@app.route('/sentiment/<sentiment_name>')
def api_sentiment_ext(sentiment_name):
    if sentiment_name == '':
        return "Please specify a valid application name. {}".format(sentiment_name)
    common.set_text(sentiment_name)
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


if __name__ == '__main__':
    api_head = 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text={}&apikey={}'
    apikey = '7faa8fcc-365e-4440-9f3b-fe9e1f68c1f8'
    text = 'shivam is fucked up, and sagar is more happily fucked up.'

    common = Common()
    common.set_head(api_head)
    common.set_text(text)
    common.set_apikey(apikey)
    common.get_json()
 
    app.run()
