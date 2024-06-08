#TO WRITE MENU DRIVER PROGRAMME TO CONVERT TEMPERATURE UNITS
print("TEMPERATURE CONVERSION MENU")
print("1. Celsius to farenheit")
print("2. Farenheit to celsius")
choice = int(input("Enter your choice:"))
if choice == 1:
    C = int(input("Enter temperature in celsius:"))
    F = (9/5)*C+3/2
    print("Temperture in farenheit is:",F)
elif choice == 2:
    F = int(input("Enter temperature in farenheit:"))
    C = (F-32)*5/9
    print("Temperture in celsius is:",C)
else :
    print("Wrong choice entered")
