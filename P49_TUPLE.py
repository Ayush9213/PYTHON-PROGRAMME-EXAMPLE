#TO INPUT TWO TUPLES AND SWAP THERE VALUES
T1=tuple()
N=int(input("Total no. of values in tuple1:"))
for i in range(N):
    A=input("Enter elements:")
    T1=T1+(A,)
T2=tuple()
N=int(input("Total no. of values in tuple2:"))
for i in range(N):
    A=input("Enter elements:")
    T2=T2+(A,)
print("First tuple:")
print(T1)
print("Second tuple:")
print(T2)
T1,T2=T2,T1
print("AFTER SWAPPING:-")
print("First tuple:")
print(T1)
print("Second tuple:")
print(T2)
