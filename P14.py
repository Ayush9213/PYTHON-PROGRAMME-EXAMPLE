#TO INPUT PERCENTAGE AND RETURN GRADE
#PERCENTAGE GRADE
#  >=90       A
#  >=80       B
#  >=70       C
#  >=60       D
#OTHERWISE    E
PER = int(input("Enter your percntage:"))
if PER >= 90:
    print("GRADE A")
elif PER >= 80:
    print("GRADE B")
elif PER >= 70:
    print("GRADE C")
elif PER >= 60:
    print("GRADE D")
else:
    print("GRADE E")
