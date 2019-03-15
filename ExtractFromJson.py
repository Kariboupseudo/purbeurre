class ExtractFromJson:

    def __init__(self, json_data):
        """ For each product i'll get : id, product_name, categories, nutrition_grade, generic_name,url """
        self.keys = [
            "id",
            "product_name",
            "categories",
            "nutrition_grades",
            "generic_name",
            "url"
            ]
        self.json_data = json_data

    def extract_json(self):
        """ Gets the brut data in the JSON returned by the API and creates a new JSON
        with only the needed data for purbeurre database """
        # list of products, will be return
        products_list = []
        # for each products i got
        for data in self.json_data["products"]:
            temp_dict = {}
            for key in self.keys:
                temp_dict[key] = data[key]                 
        products_list.append(temp_dict)

        return products_list