import mysql.connector

class Database :
    """ Creates the database """
    def __init__(self, usr, passwd, server):
        self.usr = usr
        self.passwd = passwd
        self.server = server
        self.mydb = mysql.connector.connect(host= self.server,user= self.usr,passwd=self.passwd)
        self.mycursor = self.mydb.cursor()
        
    def create_base(self):
        """ Creates the database if it doesn't exist """
        self.mycursor.execute(
            'CREATE DATABASE IF NOT EXISTS purbeurre CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        self.mycursor.execute('USE purbeurre')

    def product_tables(self):
        """ creates a table called Product with 5 different fields 
        in it if the table does not exists already """ 

        self.mycursor.execute('CREATE TABLE IF NOT EXISTS product(\
                PROD_id BIGINT PRIMARY KEY,\
                PROD_name VARCHAR(100) NOT NULL,\
                PROD_descr VARCHAR(150) NOT NULL,\
                PROD_grade CHAR(1) NOT NULL,\
                PROD_url VARCHAR(150) NOT NULL UNIQUE)')

    def category_table(self):
        """ creates a table called category with 2 different fields 
        in it if the table does not exists already """

        self.mycursor.execute('CREATE TABLE IF NOT EXISTS category(\
            CAT_id int PRIMARY KEY AUTO_INCREMENT,\
            CAT_nom VARCHAR(50) UNIQUE)')   
        


 



