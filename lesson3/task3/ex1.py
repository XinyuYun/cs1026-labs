int1 = float(input("Please enter the first integer: "))
int2 = float(input("Please enter the second integer: "))
int3 = float(input("Please enter the third integer: "))

if int1 <= int2 <= int3:
    print("ascending")
elif int1 >= int2 >= int3:
    print("descending")
else:
    print("not in order")


