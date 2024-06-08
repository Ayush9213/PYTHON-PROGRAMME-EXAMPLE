#TO CREATE A ARITHEMATIC CALCULATOR
A = int(input("ENTER A NUMBER:"))
B = int(input("ENTER A NUMBER:"))
op = input("ENTER THE OPERATOR(+,-,*,/):")
if op == '+':
    print("Addition of two numbers is:",A+B)
elif op == '-':
    print("Subtraction of two numbers is:",A-B)
elif op == '*':
    print("Multiplication of two numbers is:",A*B)
elif op == '/':
    print("Division of two numbers is:",A/B)
else :
    print("Wrong operator entered")

    
