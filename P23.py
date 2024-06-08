#TO INPUT AN INTEGER AND CHECK WEATHER
#IT IS EVEN +VE, -VE, OR ODD +VE, -VE.
N = int(input("Enter an integer:"))
if N>0:
    if N%2 == 0:
        print("EVEN POSITIVE")
    else :
        print("ODD POSITIVE")
elif N%2 == 0:
    print("EVEN NEGATIVE")
else :
    print("ODD NEGATIVE")
