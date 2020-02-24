a = int(input("Enter a number:"))
if (a >= 80 and a<=100):
    print("A+")
elif (a >= 70 and  a <= 79):
    print("A")
elif (a >= 60 and  a <= 69):
    print("A-")
elif (a >= 50 and  a <= 59):
    print("B")
elif (a >= 40 and a <= 49):
    print("C")
elif (a >= 30 and  a <= 39):
    print("D")
elif (a >= 0 and  a <30):
    print("fail")
else:
    print("Please Enter 0-100")