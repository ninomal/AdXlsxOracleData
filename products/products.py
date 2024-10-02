import pandas as pd

class Products():
    def __init__(self):
        pass
    
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
        
      

        