year=int(input("yrsOfService= "))
a=int(input("salary= "))
b=int(input("bonus= "))
if year < 5:
    if a < 500:
        b = 100
    else:
        b = 200
else:
    b = 700
    
print("Bonus amount: ", b)