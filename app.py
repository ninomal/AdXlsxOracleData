from productsService.productsService import ProductsService
from products.products import Products

def main():
    productsService = ProductsService()
    products = Products()

    print(products.readXlsx(r"path here"))

    #productsService.addDataOracle(data)
    #print(productsService.exemple())








if __name__ == "__main__":
    main()

