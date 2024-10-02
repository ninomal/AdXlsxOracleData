from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()
    rowLen = products.getLenXlsx(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx")
    #print(products.readXlsxRowSelect(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", "DIA"))
    
    #for i in range(rowLen):
        #print(products.readXlsxIloc(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", i))


    #productsService.getTableInfo('products')

    #productsService.getColumnsNames('products')
    

    data = {'id_products': 5, 'nome_products': 'samsung home', 'marca': 'samsung','categoria': 'eletronico', 'preco_unit': 500, 'custo_unit': 150}

    productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

