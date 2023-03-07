M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S > 0:
    if 1 <= S <= 100:
        b=S*M1
    if 101 <= S <= 150:
        b=M1*100+M2*(S-100)
    if 151 <= S: 
        b=M1*100+M2*50+M3*(S-150)   
        
print("Phai tra=",b)

