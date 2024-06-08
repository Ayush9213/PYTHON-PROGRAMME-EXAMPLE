#TO INPUT SALARY OF USER AND CALCULATE TAX
#   SALARY            TAX
#   >=500000           5%
#   >=400000           4%
#   >=300000           3%
#   >=OTHERWISE      NO TAX
SAL = int(input("Enter the salary:"))
if SAL >= 500000:
    TAX = 0.05*SAL
elif SAL >= 400000:
    TAX = 0.04*SAL
elif SAL >= 300000:
    TAX = 0.03*SAL
else :
    TAX = 0
print("Calculated tax is:", TAX)
    
