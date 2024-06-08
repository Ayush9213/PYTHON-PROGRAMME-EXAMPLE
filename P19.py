#TO WRITE MENU DRIVER PROGRAMME TO CLACULATE AREA AND PERIMETER OF SQUARE
print("SQUARE MENU")
print("1. Area of square")
print("2. Perimeter of square")
choice = int(input("Enter your choice:"))
if choice == 1:
    A = int(input("Enter side:"))
    print("Area of square:",A*A)
elif choice == 2:
    Side = int(input("Enter side:"))
    print("Perimeter of square:",4*Side)
else :
    print("Wrong choice entered")
