inventory = 0
while 1:
    user_input=input("Enter stock quantity or type 'quit' to exit: ")
    
    if user_input == "quit" :
        print("Ending program")
        break

    elif user_input.isdigit() == 1:
        stock = int(user_input)
        inventory += stock
        print("Current stock: ",inventory )
        if inventory>500:
            print("Inventory exceeds 500")
            break

    elif user_input.isdigit() == 0:
        print("Error please enter a non-negative integer")
  





