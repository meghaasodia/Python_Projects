while True:
    Name = input("Enter Customer's Name : ")
    Total = 0

    while True:
        print("Enter the Amount and Quantity")
        Amount = float(input("Enter the Amount : "))
        Quantity = float(input("Enter the Quantity : "))
        Total+=Amount*Quantity
        repeat =input("Do you want to add more items ? : ")
        if repeat == "no" or repeat == "No" or repeat == "NO":
            break
    print("-"*40)
    print("Name : ",Name)
    print("Amount to be Paid : ",Total)
    print("-"*40)
    print("********** HAPPY SHOPPING **********")
    repeat1 = input("Do you want to go for the next Customer ? : ")
    if repeat1 == "no" or repeat == "No" or repeat == "NO":
        break
