import cx_Oracle
from models.conection import Conection
from products.products import Products
import pandas as pd


class ProductsService():
    def __init__(self):
        self.conectionRow = Conection()
        self.conection = self.conectionRow.getConection()
        self.cursor = self.conection.cursor()
        self.products = Products()
        self.columnsName = ""
        self.dictData = {}

    def addDataOracle(self, dictData):
        try:
            insert_query = """
                INSERT INTO 
                    products(id_products, nome_products, marca, categoria, preco_unit, custo_unit)
                VALUES
                    (:id_products, :nome_products, :marca, :categoria, :preco_unit, :custo_unit)
                """
            
            self.cursor.execute(insert_query, dictData)

            # Commit the transaction
            self.conection.commit()  
            return ("Data added successfully!")

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
        
    def addOracleDataAuto(self, tableName, dictData):
        try:
            self.getColumnsNames(tableName)
            stringsInput = self.products.createColumnsAdd(self.columnsName)
            insert_query = f"""
                INSERT INTO {tableName}({stringsInput[0]})VALUES
                            ({stringsInput[1]})
                """
            self.cursor.execute(insert_query, dictData)
            
            # Commit the transaction
            self.conection.commit()  
            return ("Data added successfully!")
        
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
        
    def convertTableINString(self, tableName):
        return self.products.createColumnsAdd(tableName)

    def getTableInfo(self, name):
        try:
            insert_query = f"""SELECT * FROM {name}"""
            select = self.cursor.execute(insert_query)
            selectFetch = select.fetchall()
            return selectFetch

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)

    def getColumnsNames(self, columns):
        try:
            insert_query = f"""SELECT * FROM {columns}
                                 WHERE ROWNUM = 1"""
            
            self.cursor.execute(insert_query)
            columnsDescription = [desc[0] for desc in self.cursor.description]
            self.columnsName = columnsDescription
            return ("Column Names:", columnsDescription)

        except cx_Oracle.DatabaseError as e:
            error, = e.args
            return ("Oracle Database Error:", error.message)
    
    def closed(self):
        self.cursor.close()
        self.conection.close()

    #Xlsx methods
        
    def readXlsxRowSelect(self, path, columName):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl')
            rowData = df[df[f'{columName}']== 12]
        
            #dict FILA
            data.append(rowData.to_dict(orient='records'))
            return data[0]
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
        
    def readXlsxIloc(self, path, row):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl')
            rowData = df.iloc[row]
        
            #dict FILA
            data.append(rowData.to_dict())
            return data[0]
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
 
    def getLenXlsx(self, path):
        try:
            df= pd.read_excel(path, engine='openpyxl')
            return (len(df)-1)
        
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
    
    def getXlsxCOlmunsName(self, path):
        try:
            df = pd.read_excel(path, header=0)
            return df.columns.tolist()

        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR ")
        except IndexError:
            return ("INDEX ERROR")

    def createTableAuto(self, nameTable, stringData):
        create_table_sql = f'''
            CREATE TABLE {nameTable} (
                id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                {stringData}
            )
        '''
        try:
            self.cursor.execute(create_table_sql)
            print(f"Table '{nameTable}' created successfully.")
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Error code: {error.code}")
            print(f"Error message: {error.message}")

        # Commit the changes
        self.conection.commit()


 

          