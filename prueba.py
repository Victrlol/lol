n1=float(input("numero 1"))
n2=float(input("numero 2"))
op=str(input("operacion"))
if op=="suma":
    r=n1+n2
    print(r)
    if r>20:
        print("grande")
if op=="resta":
    r=n1-n2
    print(r)
if op=="multiplicacion":
    r=n1*n2
    print(r)
if op=="division":
    r=n1/n2
    print(r)
else:
    print("operacion no valida")