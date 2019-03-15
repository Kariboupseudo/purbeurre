import records

class DatabaseUpdator():
    """ To update tables of the Base """
    def __init__(self, data, db_connection):
        self.data = data
        self.mydb = db_connection
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute('USE purbeurre')

    def table_product_update(self):
        """ Inserts products in product table """
        for product in self.data:
            
            self.mycursor.execute('INSERT INTO product (PROD_id, PROD_name, PROD_descr, PROD_grade, PROD_url)\
                VALUES(:id, :name, :descr, :grade, :link)',
                id = product["id"],
                name = product["product_name"],
                descr = product["generic_name"],
                grade = product["nutrition_grades"],
                link = product["url"],
                )
    
    def table_category_update(self):
        """ Inserts categories in category table """
        for product in self.data: 
            categories_list = product['categories'].split(',')
            for categorie in categories_list:
                self.mycursor.execute("INSERT INTO category (CAT_nom) VALUES (:cat)", cat = categorie)

