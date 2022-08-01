#Function to print the floyd triangle based on unser input number of rows
def floyd(n): 
    num = 1
    print("\n")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{num} ", end = "")
            num += 1        
        print("")
    print("\n")
    
#loop to display the menu and get the choice of operation to be performed from the user
while(True):
    print("1. Print triangle")
    print("2. Exit")
    ch = int(input("Enter choice : "))
    match ch:
        case 1:
            #get the number of rows to be displayed from the user
            n = int(input("Enter number of rows to print(atleast 1) : "))
            if n > 0:
                #calling the function
                floyd(n)
            else: 
                #display error message and loop back to menu
                print("Number of rows cannot be less than 1!\nTry Again")
        case 2:
            print("Exiting...")
            exit()
        case _:
            print("Invalid Input!")