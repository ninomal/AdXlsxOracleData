import cx_Oracle
from models.conection import Conection

class ProductsService():
    def __init__(self):
        self.conectionRow = Conection()
        self.conection = self.conectionRow.getConection()
        self.cursor = self.conection.cursor()

    def addDataOracle(self, dictData):
        try:
            #change query and values
            insert_query = """INSERT INTO 
                        clients(clients_id, nome_client, sexo, email, idade) VALUES
                                (:clients_id, :nome_client, :sexo, :email, :idade)"""
            
            self.cursor.execute(insert_query, dictData)

            # Commit the transaction
            self.conection.commit()  
            print("Data added successfully!")

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print("Oracle Database Error:", error.message)

    def closed(self):
        self.cursor.close()
        self.conection.close()

    def exemple(self):
        return(
        '''
            EXEMPLO
            
            dictTest = {'clients_id':4, 'nome_client':'joao', 'sexo':'m',
                        'email':'joao@gamil.com', 'idade': '20/09/1980'}

            insert_query = """INSERT INTO 
                            clients(clients_id, nome_client, sexo, email, idade) VALUES
                                    (:clients_id, :nome_client, :sexo, :email, :idade)"""

            self.cursor.execute(insert_query, dictTest)

            self.conection.commit()
        ''' )
      

          