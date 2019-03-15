import json
import requests

class JsonFromApi:

    def __init__(self,category):
        self.category = category

    def get_json(self):
        """ This method generates the request,
        submits it with the library requests
        and returns a json file"""

        baseurl = 'https://fr.openfoodfacts.org/cgi/search.pl'

        params = {'action':'process', 'tagtype_1':'categories', 'tag_contains_0':'contains','tag_0': self.category, 'page_size':500,'json':1}
        
        r = requests.get(baseurl, params)
        json_data = json.loads(r.text)
        with open('RESULTS.json', 'w') as f:
            f.write(json.dumps(json_data, indent=4))
        
        return r.json()

