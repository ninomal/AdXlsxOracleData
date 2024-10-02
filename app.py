from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()
    #rowLen = productsService.getLenXlsx(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx")
    #print(productsService.readXlsxRowSelect(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", "DIA"))
    
    #for i in range(rowLen):
        #print(productsService.readXlsxIloc(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", i))

    #info tables
    #productsService.getTableInfo('products')

    #for add value in row auto
    print(productsService.getColumnsNames('products'))
    #productsService.addOracleDataAuto('products', None)




    #data = {'id_products': 5, 'nome_products': 'samsung home', 'marca': 'samsung','categoria': 'eletronico', 'preco_unit': 500, 'custo_unit': 150}
    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

