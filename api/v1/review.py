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


@app.route('/review')
def api_review():
    '''
    Remove this in future.
    '''
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


@app.route('/review/<review_name>')
def api_review_ext(review_name):
    if review_name == '':
        return "Please specify a valid application name. {}".format(review_name)
    common.set_text(review_name)
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


if __name__ == '__main__':

    api_head = 'https://data.42matters.com/api/v2.0/android/apps/lookup.json?p={}&access_token={}'
    apikey = '4b0cff026e913e19d5b3a18ac5d8523ee07d8c2f '
    package = 'com.ubercab'

    common = Common()
    common.set_head(api_head)
    common.set_text(package)
    common.set_apikey(apikey)
    common.get_json()

    app.run()
