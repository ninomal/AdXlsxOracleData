import cx_Oracle
from models.conection import Conection

class ProductsService():
    def __init__(self):
        self.conect = Conection()
        self.conection = self.conect.getConection()

    def test(self):
        id = 145
        name = 'petter'

        sql = """INSERT INTO clients(clients_id, nome_client) VALUE
                    (:id, :name)"""
        #tes = self.cursor.execute("select * from clients")
        #print(tes)