c = "admin"

try:
    a = input("Enter user name: ")
    
    if a  == c:
        print("Next")

    else:  
        for d in range(4):
            a = input("Enter user name: ")
            if a != c:
                print("Try again")

    b = input("Enter password: ")

    if b == c:
        print("Access Granted")
    
    else:  
        for d in range(3):
            b = input("Enter password: ")
            if b != c:
                print("Try again")
            
except KeyboardInterrupt as error:
    print("Try again", error)

