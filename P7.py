#TO INPUT TWO INTEGERS FROM USER AND DISPLAY THEIR VALUE
#METHOD 1
A = int(input("Enter first no:"))
B = int(input("Enter second no:"))
C = A
A = B
B = C
print("First no. is:",A)
print("Second no. is:",B)

#METHOD 2
A = int(input("Enter first no:"))
B = int(input("Enter second no:"))
A = A+B
B = A-B
A = A-B
print("First no. is:",A)
print("Second no. is:",B)

#METHOD 3
A = int(input("Enter first no:"))
B = int(input("Enter second no:"))
A,B = B,A
print("First no. is:",A)
print("Second no. is:",B)
