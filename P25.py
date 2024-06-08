#TO INPUT UNITS CONSUMED AND CALCULATE ELECTRICITY BILL
#METER CHARGES = 150
#  NO. OF UNITS       CHARGES(IN PAISE)
#  FIRST 1OO UNITS       40
#  NEXT 200 UNITS        50
#  BEYOND 300 UNITS      60
N = int(input("Enter no. of units:"))
if N<=100:
    bill = N*0.4+150
elif N<300:
    bill = 100*0.4+(N-100)*0.5+150
else :
    bill = 100*0.4+200*0.5+(N-300)*0.6+150
print("Calculated electricity bill is:",bill)
