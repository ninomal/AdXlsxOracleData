from enums.enumsTypes import EnumsType


class Products():
    def __init__(self):
        self.enumsType = EnumsType()
   
    def createColumnsAdd(self, columnsName):
        stringList = []
        stringRow = ', '.join(column for column in columnsName)
        stringList.append(stringRow)
        columnsName[0] = f":{columnsName[0]}"
        stringRowValues = ', :'.join(column for column in columnsName)
        stringList.append(stringRowValues)
        print(stringList)
        return stringList

    def createTable(self, listOfColumns):
        print(self.enumsType.getAllEnumsType())
        print(self.enumsType.enumType(1))
      

        