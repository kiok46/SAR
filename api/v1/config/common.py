'''
Team: Atom

@Author Kuldeep Singh Grewal <kuldeepbb.grewal@gmail.com>
'''

import json
from urllib import urlopen


class Common():

    api_head = ''
    apikey = ''
    text = ''

    def set_head(self, api_head):
        self.api_head = api_head

    def set_text(self, text):
        self.text = text

    def set_apikey(self, apikey):
        self.apikey = apikey

    def get_api(self):
        return self.api_head.format(self.text, self.apikey)

    def get_json(self):
        api = self.get_api()
        rs = urlopen(api).read()
        result = json.loads(rs)
        out_file = open("reviews.json", "w")
        json.dump(result, out_file, indent=4)
        out_file.close()
