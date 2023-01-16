def numero():
    n = int(input("Escolhe um número! "))
    bn=[]

    while n > 0:
        bn.append(n % 2)
        n = n//2
    
    bn.reverse()
    
    while len(bn) < 8:
        bn.insert(0, 0)
    
    resultado = ''.join(str(i) for i in bn)

    print(resultado)

x = 10
while x > 2:
    numero()