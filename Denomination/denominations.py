denominations = [2000,500,100,50,20,10,5,2,1] 

def calc(m):
    temp = m
    print("\n")
    for i in denominations:
        n = temp//i
        if (n != 0):
            print(f"\n{i} notes is: {n}") 
        temp = temp%i
    print("\n")

while(True):
    print("1. Calculate notes and coins")
    print("2. Exit")
    ch = int(input("Enter choice : "))
    match ch:
        case 1:
            m = int(input("Ener the amount : "))
            calc(m)
        case 2:
            exit()
        
