while True:
    menu = {'Pizza': 100,
        'Pasta': 150,
        'Burger': 50,
        'Salad': 40,
        'Momos': 70,
        'Chilli Potato': 70,
        'Spring Roll': 60,
        'Manchurian': 90,
        'Fried Rice': 50,
        'Chowmein': 80,
        'Hot Coffee': 80,
        'Cold Coffee': 80,
        'Cold Drink': 80,
    }
    print("Welcome To Our New PYTHON Restaurant")
    print("""
          Pizza           : Rs.100
          Pasta           : Rs.150
          Burger          : Rs.50
          Salad           : Rs.40
          Momos           : Rs.70
          Chilli Potato   : Rs.70
          Spring Roll     : Rs.60
          Manchurian      : Rs.90
          Fried Rice      : Rs.50
          Chowmein        : Rs.80
          Hot Coffee      : Rs.80
          Cold Coffee     : Rs.80
          Cold Drink      : Rs.80""")

    Name = input("Enter your Name : ")
    Total_Order = 0

    while True:
        Item_1 = input("Enter the name of food item you want to order : ")
        Total_Order += menu[Item_1]
        repeat =input("Do you want to add more items ? : ")
        if repeat == "no" or repeat == "No" or repeat == "NO":
                break
        if Item_1 in menu:
                print(f"*** Your food item {Item_1} has been added to your order ***")
        else:
                print(f"Ordered item {Item_1} is not available yet!") 
            
    print("-"*40)
    print("Name : ",Name)
    print("Total Amount to be Paid : ",Total_Order)
    print("-"*40)
    print("********** THANK YOU FOR VISIT **********")
    print("************* VISIT AGAIN *************")
    repeat1 = input("Do you want to go for the next Customer ? : ")
    if repeat1 == "no" or repeat == "No" or repeat == "NO":
        break
