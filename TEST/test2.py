CORRECT_USER = "admin"
CORRECT_PASS = "admin"  # Using 'admin' as password based on your variable 'c'

try:
    # --- PHASE 1: USERNAME CHECK (4 ATTEMPTS) ---
    username_success = False
    
    for attempt in range(4):
        user_input = input("Enter user name: ")
        
        if user_input == CORRECT_USER:
            print("Next")
            username_success = True
            break  # Exit the username loop immediately
        else:
            # Only print "Try again" if they have attempts left
            if attempt < 3:
                print("Try again")
            else:
                print("Access Denied: Too many username attempts.")

    # --- PHASE 2: PASSWORD CHECK (4 ATTEMPTS) ---
    if username_success:
        password_success = False
        
        for attempt in range(4):
            pass_input = input("Enter password: ")
            
            if pass_input == CORRECT_PASS:
                print("Access Granted")
                password_success = True
                break  # Exit the password loop immediately
            else:
                if attempt < 3:
                    print("Try again")
                else:
                    print("Access Denied: Too many password attempts.")

except KeyboardInterrupt:
    print("\nProgram interrupted.")