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


@app.route('/search')
def api_search():
    '''
    Remove this in future.
    '''
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


@app.route('/search/<search_name>')
def api_search_ext(search_name):
    if search_name == '':
        return "Please specify a valid application name. {}".format(search_name)
    common.set_text(search_name)
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.loads(rs)
    return '{}'.format(result)


if __name__ == '__main__':
    api_head = 'https://data.42matters.com/api/v2.0/android/apps/search.json?q={}&include_developer=false&include_desc=false&limit=5&access_token={}'
    apikey = '4b0cff026e913e19d5b3a18ac5d8523ee07d8c2f '

    common = Common()
    common.set_head(api_head)
    common.set_apikey(apikey)
    app.run()
