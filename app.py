from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()

    print(products.readXlsx(r"D:\Users\User\Desktop\CURSO PYTON\DiarioPython\2024.xlsx"))

    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

