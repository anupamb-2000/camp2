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
        self.tax_percent = self.tax/self.basic_price * 100 
        self.discount_percent = self.discount/self.MRP * 100
        self.checkCapacity(capacity)
        Product.products[self.product_code] = [self.name,self.category, self.basic_price, self.tax_percent, self.tax, self.discount_percent, self.discount, self.MRP]

    def displayProducts(self):
        print("-------------------------------------------------")
        for key,val in Product.products.items():
            print(f"Product Code : {key}\nProduct Name : {val[0]}\nCategory : {val[1]}\nBasic Price : {val[2]}\nTax percent: {val[3]}\nTax amount: {val[4]}\nDiscount percent: {val[5]}\nDiscount amount: {val[6]}\nMRP : {val[7]}")
            print("-------------------------------------------------")


def getCategory():
    categories = ['HYGIENE', 'HEALTH', 'STAPLES', 'SPORTS', 'FASHION']
    category = input("Enter category name : ").upper()
    if category in categories:
        return category
    else:
        print("Invalid category!")
        exit()

def getDiscountAmt():
    print("Choice of input ")
    print("1. Discount amount")
    print("2. Discount percent")
    coi = int(input("CHOICE : "))
    if (coi == 1):
        discount = float(input("Enter discount amount : "))
    elif (coi == 2):
        discount = float(input("Enter discount percent : "))/100 * MRP
    return discount

def getTaxAmount():
    print("Choice of input ")
    print("1. Tax amount")
    print("2. Tax percent")
    coi = int(input("CHOICE : "))
    if (coi == 1):
        tax = float(input("Enter tax amount : "))
    elif (coi == 2):
        tax = float(input("Enter tax percent : "))/100 * basic_price
    return tax

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
            category = getCategory()
            print("Choice of input ")
            print("1. MRP")
            print("2. Basic Price")
            coi = int(input("CHOICE : "))
            if (coi == 1):
                MRP = float(input("Enter MRP : "))
                discount = getDiscountAmt()
                tax = getTaxAmount()
                basic_price = MRP - tax
            elif (coi == 2):
                basic_price = float(input("Enter basic price : "))
                tax = getTaxAmount()
                MRP = basic_price + tax
                discount = getDiscountAmt()
            pro.addProduct(name, category, basic_price, tax, discount, MRP)
            print("Record Added!")

        case 3:
            exit()
        case _:
            print("Invalid input!")