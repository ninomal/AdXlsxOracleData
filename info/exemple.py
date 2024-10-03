class Exemples():
    def __init__(self):
        pass
        
    def exempleOfInnsertInto(self):
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