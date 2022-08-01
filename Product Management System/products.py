from itertools import product
import random

class Product:
    products = {}

    def checkCapacity(self, capacity):
        count = 0
        for key,val in Product.products.items():
            if (val[1] == self.category):
                count += 1
        if count >= capacity:
            print("Capacity Exceeded!")
            exit()

    def getRandomNumber(self):
        number = random.randint(100,999)
        return str(number)
    
    def getProductCount(self):
        count = 0
        for key,val in Product.products.items():
            if (val[0] == self.name and val[1] == self.category):
                count += 1
        return str(count)

    def addProduct(self, name, category, basic_price, tax, discount, MRP):
        self.name = name.upper()
        self.category = category.upper()
        self.product_code = self.name[0:2] + self.category[0:2] + self.getProductCount() + self.getRandomNumber()
        self.basic_price = basic_price
        self.tax = tax
        self.discount = discount
        self.MRP = MRP
        self.checkCapacity(capacity)
        Product.products[self.product_code] = [self.name,self.category, self.basic_price, self.tax, self.discount, self.MRP]

    def displayProducts(self):
        print("-------------------------------------------------")
        for key,val in Product.products.items():
            print(f"Product Code : {key}\nProduct Name : {val[0]}\nCategory : {val[1]}\nBasic Price : {val[2]}\nTax : {val[3]}\nDiscount : {val[4]}\nMRP : {val[5]}")
            print("-------------------------------------------------")


capacity = int(input("Enter maximum capacity : "))
while(True):
    print("\nMenu : ")
    print("1. List all products")
    print("2. Add a product")
    print("3. Exit")
    ch = int(input("Enter your choice : "))
    pro = Product()
    match ch:
        case 1:
            pro.displayProducts()
        case 2:
            name = input("Enter name of the product : ")
            category = input("Enter category name : ")
            basic_price = float(input("Enter basic price : "))
            tax = float(input("Enter tax : "))
            discount = float(input("Enter discount : "))
            MRP = float(input("Enter MRP : "))
            pro.addProduct(name, category, basic_price, tax, discount, MRP)
        case 3:
            exit()
        case _:
            print("Invalid input!")