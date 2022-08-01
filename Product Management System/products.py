class Product:
    products = []
    def __init__(self, name, category, basic_price, tax, discount, MRP):
        self.name = name.upper()
        self.category = category.upper()
        self.product_code = name[0:2] + category[0:2] + getProductCount(name, category) + getRandomNumber()
        self.basic_price = basic_price
        self.tax = tax
        self.discount = discount
        self.MRP = MRP

    def getProductCount(self, name, category):
        

while(True):
    print("Menu : ")
    print("1. List all products")
    print("2. Add a product")
    print("3. Exit")
    ch = int(input("Enter your choice : "))
    match ch:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case _:
            print("Invalid input!")