solt = []
casad = []
divor = []
viuv = []
cont = 0

while cont < 20:
    nome = input('Digite seu nome: ')
    estado_civil = input('Digite seu estado civil: ')

    if (estado_civil.lower() == 'solteiro') or (estado_civil.lower() == 'solteira'):
        solt.append(nome)
    elif (estado_civil.lower() == 'casado') or (estado_civil.lower() == 'casada'):
        casad.append(nome)
    elif (estado_civil.lower() == 'divorciado') or (estado_civil.lower() == 'divorciada'):
        divor.append(nome)
    elif (estado_civil.lower() == 'viuvo') or (estado_civil.lower() == 'viuva'):
        viuv.append(nome)
    else:
        print('ERRO! Estado civil inválido')
        cont = cont - 1
    cont = cont + 1
print(f'SOLTEIROS(AS):\n{solt}')
print(f'CASADOS(AS):\n{casad}')
print(f'DIVORCIADOS(AS):\{divor}')
print(f'VIÚVOS(AS):\n{viuv}')
