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

    # ADD in string output and mescle two list for create table
    def createTable(self, listOfColumns, listOfEnumsTypes):
        stringMescle =''
        for row in range(len(listOfColumns)):
            enumsType = self.enumsType.type(listOfEnumsTypes[row])
            if row == len(listOfColumns)- 1:
                stringMescle += f'{listOfColumns[row]} {enumsType}'
            else:
                stringMescle += f'{listOfColumns[row]} {enumsType} , \n'
        return stringMescle
    
    def getEnumsType(self):
        return self.enumsType.getAllEnumsType()

        