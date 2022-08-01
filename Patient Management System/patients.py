import pyodbc

#create a connection string
myConString = 'Driver={SQL Server};Server=DESKTOP-517KMB6\SQLEXPRESS;Database=patients_db;Trusted_Connection=yes;'

def validateInt(i):
    if len(i) != 0:
        return int(i)
    return int(validateInt(input("Input cannot be blank!\nEnter again : ")))

def validate(i):
    if len(i) != 0:
        return i   
    return validate(input("Input cannot be blank!\nEnter again : "))

def display(mycursor):
    #Displaying the results
    patients = [{'Patient ID': row[0], 'Name': row[1], 'Gender': row[2], 'Age': row[3], 'Blood Group': row[4]} for row in mycursor.fetchall()]
    print("--------------------------------------------------------------------")
    print("Patient Id \t Patient Name \t Gender \t Age \t Blood Group")
    for record in patients:
        print(f"{record['Patient ID']} \t\t {record['Name']} \t\t {record['Gender']} \t\t {record['Age']} \t\t {record['Blood Group']}")
    print("--------------------------------------------------------------------")

def listPatients():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        #get the contents 
        mycursor.execute("SELECT * FROM patients ORDER BY patientName")
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        #saving the result into a dictionary
        display(mycursor)
    myconn.commit()
    myconn.close()

def addPatient():
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        #insert into the table
        mycursor.execute(f"EXEC insertPatient {id}, '{name}', '{gender}', {age}, '{bg}'")
    except Exception as e:
        if type(e).__name__ == "IntegrityError":
            print("ERROR : Duplicate patient Id entered")
        else:
            print(f"{type(e).__name__}")
            print(e)
    else:
        print("Record added!")

    myconn.commit()
    myconn.close()

def searchPatient(id):
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        mycursor.execute(f"EXEC search {id}")

        rows = mycursor.rowcount
        
        if rows != 0:
            try:
                mycursor.execute(f"EXEC search {id}")
                
            except Exception as e:
                print(f"{type(e).__name__}")
            else:
                display(mycursor)
        else:
            print("No such record found!")
    except Exception as e:
        print(f"{type(e).__name__}")
        print(e)

    myconn.commit()
    myconn.close()

def deletePatient(id):
    #create a connection with the connection string
    myconn = pyodbc.connect(myConString)
    try: 
        #get the cursor object
        mycursor = myconn.cursor()
        mycursor.execute(f"EXEC search {id}")

        rows = mycursor.rowcount
        
        if rows != 0:
            try:
                mycursor.execute(f"EXEC deletePatient {id}")            
            except Exception as e:
                print(f"{type(e).__name__}")
            else:
                print("Record deleted successfully!")
        else:
            print("No such record found!")
    except Exception as e:
        print(f"{type(e).__name__}")
        print(e)

    myconn.commit()
    myconn.close()


#create a connection with the connection string
myconn = pyodbc.connect(myConString)

myconn.commit()
myconn.close()

#Displaying Menu for the user
while(True):
    print("Menu :")
    print("\t1. List all patients")
    print("\t2. Add a new patient")
    print("\t3. Search patient")
    print("\t4. Delete patient")
    print("\t5. Exit")
    choice = int(input("Enter your choice:"))
    match choice:
        case 1:
            listPatients()
        case 2:
            id = validateInt(input("Enter id : "))
            name = input("Enter the name : ")
            gender = input("Enter gender : ")
            age = int(input("Enter age : "))
            bg = input("Enter blood group : ")
            addPatient()
        case 3:
            id = int(input("Enter id of patient to search : "))
            searchPatient(id)
        case 4:
            id = int(input("Enter id of patient to delete : "))
            deletePatient(id)
        case 5:
            exit()
        case _:
            print("Invalid Input!")