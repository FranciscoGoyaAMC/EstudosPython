val1 = int(input('Digite um número: '))
val2 = int(input('Digite outro número: '))

if val1 < val2:
    print(f'Valores entre {val1} e {val2}')
    for i in range(val1,val2+1):
        print(i)

else:
    print(f'Valores entre {val2} e {val1}')
    for i in range(val2,val1+1):
        print(i)
