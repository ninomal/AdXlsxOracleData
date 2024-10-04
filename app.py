from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()
    #print(productsService.readXlsxRowSelect(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", "DIA"))
    
    #rowLen = productsService.getLenXlsx(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx")
    #for i in range(rowLen):
        #print(productsService.readXlsxIloc(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", i)['DIA'])

    #info tables
    #info = productsService.getTableInfo('products')
    #print(info)

    #for create table
    print(productsService.getXlsxCOlmunsName(r"C:\Users\ninomal\Documents\products.xlsx"))
    listOfColumns = productsService.getXlsxCOlmunsName(r"C:\Users\ninomal\Documents\products.xlsx")
    print('\n\n\n\'', products.getEnumsType())
    listCreateTable = [1, 1, 3, 2]
    #print(products.createTable(listOfColumns, listCreateTable))
    stringDataCreateTable = products.createTable(listOfColumns, listCreateTable)
    productsService.createTableAuto('products2', stringDataCreateTable)







    #for add value in row auto
    #print(productsService.getColumnsNames('products'))
    #data = {'ID_PRODUCTS': 6, 'NOME_PRODUCTS':'phone razer', 'MARCA':'RAZER',
            #'CATEGORIA':'microhpone', 'PRECO_UNIT': 800, 'CUSTO_UNIT': 450}
    #print(productsService.addOracleDataAuto('products', data))




    #data = {'id_products': 5, 'nome_products': 'samsung home', 'marca': 'samsung','categoria': 'eletronico', 'preco_unit': 500, 'custo_unit': 150}
    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

