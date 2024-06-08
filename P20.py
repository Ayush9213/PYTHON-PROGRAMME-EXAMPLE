#TO INPUT A YEAR FROM USRE AND CHECK, IS IT LEAP YEAR
Year = int(input("Enter a year:"))
if Year%4 == 0 and Year%100!=0:
    print("LEAP YEAR")
elif Year%400 == 0:
    print("LEAP YEAR")
else :
    print("NOT A LEAP YEAR")
