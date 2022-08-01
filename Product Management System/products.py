class Product:
    products = []

    def getRandomNumber(self):
        return str(123)
    
    def getProductCount(self, name, category):
        count = 0
        for product in Product.products:
            if (product["Name"] == name and product["category"] == category):
                count += 1
        return str(count)

    def temp(self):
        print(self.name)
        print(self.product_code)

    def __init__(self, name, category, basic_price, tax, discount, MRP):
        self.name = name.upper()
        self.category = category.upper()
        self.product_code = self.name[0:2] + self.category[0:2] + self.getProductCount(name, category) + self.getRandomNumber()
        self.basic_price = basic_price
        self.tax = tax
        self.discount = discount
        self.MRP = MRP


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
            name = input("Enter name of the product : ")
            category = input("Enter category name : ")
            basic_price = float(input("Enter basic price : "))
            tax = float(input("Enter tax : "))
            discount = float(input("Enter discount : "))
            MRP = float(input("Enter MRP : "))
            pro = Product(name, category, basic_price, tax, discount, MRP)
            pro.temp()
        case 3:
            exit()
        case _:
            print("Invalid input!")