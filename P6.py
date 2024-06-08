#TO INPUT TIME IN SECONDS AND DISPLAY IN MINUTES AND SECONDS
T = int(input("Enter time in seconds:"))
Min = T//60
Sec = T%60
print("Minutes in given time:",Min)
print("Remaining seconds in given time:",Sec)
