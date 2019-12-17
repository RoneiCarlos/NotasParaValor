x = int(input('digite um valor\n'))

cont = 0

notas = None

while x >= 100:
    cont += 1
    y = x - 100
    x = y

notas = f'{str(cont)} - nota(s) de 100\n'

cont = 0

while x >= 50:
    cont += 1
    y = x - 50
    x = y

notas += f'{str(cont)} - nota(s) de 50\n'

cont = 0

while x >= 20:
    cont += 1
    y = x - 20
    x = y

notas += f'{str(cont)} - nota(s) de 20\n'

cont = 0

while x >= 10:
    cont += 1
    y = x - 10
    x = y

notas += f'{str(cont)} - nota(s) de 10\n'

cont = 0

while x >= 5:
    cont += 1
    y = x - 5
    x = y

notas += f'{str(cont)} - nota(s) de 5\n'

cont = 0

while x >= 2:
    cont += 1
    y = x - 2
    x = y

notas += f'{str(cont)} - nota(s) de 2\n'

cont = 0

while x >= 1:
    cont += 1
    y = x - 1
    x = y

notas += f'{str(cont)} - nota(s) de 1'

print(notas)
