import json
import requests
import random

class Apiextract:

    def __init__(self):
        self.info = None
       
    def get_categories(self):
        """Get all french categories containing 10 products, 
        and whose name is not longer than 15 characters from 
        the french Open Food Facts database.
        Results are stored in a JSON file
        """
        FilteredCat=[]
        RandomCat=[]
        url = 'https://fr.openfoodfacts.org/categories.json'
        data = requests.get(url).json()
        for categorie in data['tags']:
            if categorie['products'] == 10: 
                name = categorie['name']
                if len(name) <= 15:
                    FilteredCat.append(categorie)
        Result = random.sample(FilteredCat, 5)
        with open('categoriesfiltered.json', 'w') as f:
            f.write(json.dumps(Result, indent=4))

    def get_products(self):
        ProductList=[]
        with open('categorychosen.json', 'r') as f:
            categories = json.load(f)
        with open('products.json', 'w') as f:
            for category in categories:
                url = category['url']
                for i in url:
                    request_url = url + "/" + str(i) + ".json"
                    data = requests.get(request_url).json()
                    ProductList.append(data)
            f.write(json.dumps(ProductList, indent=4))