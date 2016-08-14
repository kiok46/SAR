'''
Team: Atom

@author Kuldeep Singh Grewal <kuldeepbb.grewal@gmail.com>
'''

from flask import Flask, url_for, render_template
from config.common import Common
import json
from urllib import urlopen

app = Flask(__name__)


@app.route('/')
def api_domain():
    return render_template('main.html')


@app.route('/google_play/<package_name>')
def api_google_data(package_name):
    from oauth2client.client import OAuth2WebServerFlow
    flow = OAuth2WebServerFlow(client_id='201223294714-5pjkgq831njk0sk2hhevckko6d1ee42o.apps.googleusercontent.com',
                               client_secret='IcEqAGbiEtpXO8CHk5a2EArV',
                               scope='https://www.googleapis.com/auth/androidpublisher',
                               redirect_uri='http://localhost:5000')

    auth_uri = flow.step1_get_authorize_url()
    return auth_uri


@app.route('/sentiment/<statement>')
def api_sentiment_ext(statement):
    if statement == '':
        return "Please specify a valid application name.{}".format(statement)

    api_head = 'https://api.havenondemand.com/1/api/sync/analyzesentiment' + \
               '/v1?text={}&apikey={}'
    apikey = '7faa8fcc-365e-4440-9f3b-fe9e1f68c1f8'

    common = Common()
    common.set_head(api_head)
    common.set_text(statement)
    common.set_apikey(apikey)
    api = common.get_api()
    rs = urlopen(api).read()
    result = json.dumps(json.loads(rs))
    return '{}'.format(result)


@app.route('/review/<review_name>')
def api_review_ext(review_name):
    if review_name == '':
        return "Please specify a valid application name.{}".format(review_name)

    api_head = 'https://data.42matters.com/api/v2.0/android/apps/' + \
               'lookup.json?p={}&access_token={}'
    apikey = '4b0cff026e913e19d5b3a18ac5d8523ee07d8c2f '

    common = Common()
    common.set_head(api_head)
    common.set_apikey(apikey)
    common.set_text(review_name)

    api = common.get_api()
    rs = urlopen(api).read()
    result = json.dumps(json.loads(rs))
    return '{}'.format(result)


@app.route('/search/<search_name>')
def api_search_ext(search_name):
    if search_name == '':
        return "Please specify a valid application name.{}".format(search_name)

    api_head = 'https://data.42matters.com/api/v2.0/android/apps/' + \
               'search.json?q={}&include_developer=false&' + \
               'include_desc=false&limit=8&access_token={}'
    apikey = '823aafff0eabb49e60edba8bc94ff153712c6104'

    common = Common()
    common.set_head(api_head)
    common.set_apikey(apikey)
    common.set_text(search_name)

    api = common.get_api()
    rs = urlopen(api).read()
    # result = json.dumps(json.loads(rs))
    # print result[0]
    # for i in result['results']:
    #    print i
    # print result
    dict_ = {}
    package_name_ = []
    title_ = []
    icon_ = []
    description_ = []

    result_ = json.loads(rs)
    out_file = open("search.json", "w")
    json.dump(result_, out_file, indent=4)
    out_file.close()

    for i in result_['results']:
        package_name_.append(i['package_name'].encode('utf-8'))
        title_.append(i['title'].encode('utf-8'))
        icon_.append(i['icon'].encode('utf-8'))
        description_.append(i['description'].encode('utf-8'))
    # print result_['results']

    dict_["package_name"] = package_name_
    dict_["title"] = title_
    dict_["icon"] = icon_
    dict_["description"] = description_

    # d = json.dumps(json.loads(dict_))
    return '{}'.format(json.dumps(dict_))


if __name__ == '__main__':
    app.run()
