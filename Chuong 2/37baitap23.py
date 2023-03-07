import math 
print("Nhap hai canh ke cua tam giac vuong: ")
b=float(input())
c=float(input())
print("Canh ke thu nhat la: ",str(b),", canh ke thu hai la: ",str(c),end="")
d=float(math.sqrt(b*b+c*c))
print(", co canh huyen = ",round(d,2))