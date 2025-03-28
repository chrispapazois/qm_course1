#askisi deuterovathmia exiswsh

#zitame ta a,b,c apo ton xrhsth ths exiswshs ax^2+2bx+c=0

a=input("a=")
b=input("b=")
c=input("c=")
print("tha lusoume tin exiswsh: \n")
print("{}x**2+{}x+{}=0".format(a,b,c))
a=float(a)
b=float(b)
c=float(c)
if a==0:
    if b==0:
        if c==0:
            print("uparxoun apeires luseis")
        else:
            print("den uparxoun luseis")
    else:
            print("oi luseis einai x1=x2={:1.2f}".format(-c/b))
        

diak=b**2-4*a*c
print("h diakrinousa einai {:1.2f}".format(diak))

if diak<0:
    print("h exiswsh den exei pragmatikes luseis")
else:
    x1= (-b+diak**0.5)/(2*a)
    x2= (-b+-iak**0.5)/(2*a)
    print ("oi luseis einai:x1= {:1.2f},x2={:1.2f}".format(x1,x2))

    
         
