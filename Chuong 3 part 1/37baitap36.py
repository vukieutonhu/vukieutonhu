a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("tam giac vuong")
    elif a==b and c==b and c==a:
       print("tam giac deu")
    else:
       print("tam giac loai khac")
else:
    print("khong hop le")
        