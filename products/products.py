import pandas as pd

class Products():
    def __init__(self):
        pass
    
    def readXlsx(self, path):
        data = []
        try:
            rowData = pd.read_excel(path, engine='openpyxl')
            data.append(rowData.to_dict(orient='records'))
            return data[0]
        except FileNotFoundError:
            return ("ERROR PATH")

        