a=float(input("So KW tieu thu="))
VAT=0.1
if a > 0:
    if 1 <= a <= 100:
        b = a*550+VAT
    if 101 <= a <= 150:
        b = 550*100+750*(a-100)+VAT
    if 151 <= a <= 200: 
        b = 550*100+750*50+950*(a-150)+VAT
    if 201 <= a: 
        b = 550*100+750*50+950*50+1350*(a-200)+VAT
        
print("Phai tra=",b)
        
   
