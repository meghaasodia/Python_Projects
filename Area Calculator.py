while True:
    print("******AREA CALCULATOR******")
    print("""Press  1  to get Area of Square
Press  2  to get Area of Rectangle
Press  3  to get Area of Circle
Press  4  to get Area of Triangle""") 
    choice = int(input("Enter a Number between 1-4 : "))
    if choice==1:
        Side = float(input("Enter the length of one Side : "))
        Area = Side*Side
        print("Formula of Square is <<Area = Side*Side>>")
        print("Area of Square is : ",Area)
    elif choice==2:
        Length = float(input("Enter the length of Rectangle : "))
        Width = float(input("Enter the width of Rectangle : "))
        Area = Length*Width
        print("Formula of Rectangle is <<Area = Length*Width>>")
        print("Area of Rectangle is : ",Area)
    elif choice==3:
        Radius = float(input("Enter the Radius of Circle : "))
        Area = ((22/7)*(Radius**2))
        print("Formula of Circle is <<Area = ((22/7)*(Radius**2))>>")
        print("Area of Circle is : ",Area)
    elif choice==4:
        Base = float(input("Enter the Base of Triangle : "))
        Height = float(input("Enter the Height of Triangle : "))
        Area = 0.5*Base*Height
        print("Formula of Triangle is <<Area = 0.5*Base*Height>>")
        print("Area of Triangle : ",Area)
    else:
        print("Invalid Input")
    repeat = input("Do you want to Calculate another Area? : ")
    if repeat=="no" or repeat=="No" or repeat=="NO":
        break
    


