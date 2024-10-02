from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()
    rowLen = products.getLenXlsx(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx")
    #print(products.readXlsxRowSelect(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", "DIA"))
    
    for i in range(rowLen):
        print(products.readXlsxIloc(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx", i))

    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

