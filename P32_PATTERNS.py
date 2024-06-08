#PROGRAMME TO PRINT PATTERNS
print("!!! PATTERN 1!!!")
i=2
while i >=0:
    j=2
    while j >=0:
        print(2,end= " ")
        j=j-1
    print()
    i=i-1

print("!!! PATTERN 2 !!!")
for i in range(1,6):
    for j in range(1,1+i):
        print(j,end=" ")
    print()

print("!!! PATTERN 3 !!!")
for i in range(1,11,2):
    for j in range(1,i+1,2):
        print(i,end= " ")
    print()

print("!!! PATTERN 4 !!!")    
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end= " ")
    print()
    
