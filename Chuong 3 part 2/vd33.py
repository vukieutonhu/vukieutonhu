i=1
while i<=9:
    j=1
    while j<=9:
        print(str(i*j).rjust(4),end=" ")
        j=j+1
    print("\n")
    i=i+1