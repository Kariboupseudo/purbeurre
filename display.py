import json
from database import *
from apiextract import *

class Display:
    """ Manages the user interface """
    def __init__(self):

        #config files with categories and login info for the database
        with open("./config.json", "r") as f:
            self.config = json.load(f)
        with open("./categoriesfiltered.json","r") as k:
            self.categories = json.load(k)

        # New instance of the database
        self.purbeurre = Database(
            self.config["user"], self.config["passwd"], self.config["server"])
        self.purbeurre.create_base()
        self.purbeurre.product_tables()
        self.purbeurre.category_table()

    def cat_choice(self):
        """ Shows categories an get user choice """
        catdict={}
        registeredchoice = []
        cat_num = 0
        user_input = None
        print("Input a number to choose a category:")

        for category in self.categories:
            name = category['name']
            print("For category {} type {}".format(name, cat_num))
            catdict[name] = cat_num
            cat_num += 1
        user_input = input(">")
        
        if int(user_input) >= 0 and int(user_input) <= cat_num:
            for category in self.categories:
                for k, v in catdict.items():
                    if int(user_input) == int(v) and category['name'] == k:
                        registeredchoice.append(category)
            with open('categorychosen.json', 'w') as f:
                f.write(json.dumps(registeredchoice, indent=4))
            return registeredchoice

def main():
    # Starts a new session setup the database / update it if asked
    renewjson = Apiextract()
    renewjson.get_categories()
    purbeurre = Display()
    # Shows the category menu / returns the chosen category
    category_chosen = purbeurre.cat_choice()
    renewjson.get_products()

main()