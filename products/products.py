
class Products():
    def __init__(self):
        pass
   
    def createColumnsAdd(self, columnsName):
        stringList = []
        stringRow = ', '.join(column for column in columnsName)
        stringList.append(stringRow)
        stringRowValues = ', :'.join(column for column in columnsName)
        stringList.append(stringRowValues)
        return stringList

      

        