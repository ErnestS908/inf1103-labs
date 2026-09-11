inventory = 0
rejected = 0
while 1:
    user_input=input("Enter stock quantity or type 'quit' to exit: ")
    
    if user_input == "quit" :
        print("Ending program")
        print("Total number of rejected errors this cycle: ", rejected)
        print("Total units processed: ", inventory)
        break

    elif user_input.isdigit() == 1:
        stock = int(user_input)
        inventory += stock
        if inventory>500:
            print("Inventory exceeds 500")
            break

    elif user_input.isdigit() == 0:
        print("Error please enter a non-negative integer")
        rejected += 1
  





