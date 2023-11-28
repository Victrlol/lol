n1=float(input("numero 1"))
n2=float(input("numero 2"))
n3=float(input("numero 3"))
op=str(input("operacion"))
if op=="suma":
    r=n1+n2+n3
if op=="resta":
    r=n1-n2-n3
if op=="multiplicacion":
    r=n1*n2*n3
if op=="division":
    r=n1/n2/n3
else:
    print("operacion no valida")
print(op)
