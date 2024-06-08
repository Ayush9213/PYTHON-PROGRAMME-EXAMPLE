"""TO INPUT GRADE FROM USER AND DISPLA REMARK
REMARKS      GRADE
Excellent    A
Good         B
Fair         C
Poor         D     ."""
Grade = input("Enter your grade:")
if Grade == 'A':
    print("EXCELLENT")
elif Grade == 'B':
    print("GOOD")
elif Grade == 'C':
    print("FAIR")
elif Grade == 'D':
    print("POOR")
else :
    print("Wrong Grade Entered")

