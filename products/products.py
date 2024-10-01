import pandas as pd

class Products():
    def __init__(self):
        pass
    
    def readXlsx(self, path):
        data = []
        try:
            df= pd.read_excel(path, engine='openpyxl')
            rowData = df[df['DIA']== 12]
            #data.append(rowData.to_dict(orient='records'))
            #return data[0]

            #dict FILA
            data.append(rowData.to_dict(orient='records'))
            return data[0]
        except FileNotFoundError:
            return ("ERROR PATH")
        except ValueError:
            return ("Valuer ERROR")
        except IndexError:
            return ("INDEX ERROR")
      

        