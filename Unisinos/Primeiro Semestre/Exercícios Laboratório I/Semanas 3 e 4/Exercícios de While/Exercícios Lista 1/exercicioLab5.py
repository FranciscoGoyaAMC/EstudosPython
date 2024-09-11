cont = 0
gremistas = 0
while cont < 10:
    time = input('Digite seu time: ').upper()
    if time == 'GREMIO' or time.upper() == 'GRÊMIO':
        gremistas += 1
    cont += 1
print("A cada 10 pessoas, {} são gremistas".format(gremistas))
