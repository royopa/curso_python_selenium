# Escrever um programa que peça dois números inteiro e um número float
# mostrar
# - o produto do dobro do primeiro com metade do segundo
# - a soma do triplo do primeiro com o terceiro
# - o terceiro elevado ao cubo

numero_um = input('Digite o primeiro número (inteiro): ')
numero_um = int(numero_um)

numero_dois = input('Digite o segundo número (inteiro): ')
numero_dois = int(numero_dois)

numero_tres = input('Digite o terceiro número (float): ')
numero_tres = float(numero_tres)

print(f'Números digitados: {numero_um}, {numero_dois} e {numero_tres}')

print(f'O produto do dobro do primeiro ({numero_um}) com metade do segundo ({numero_dois})')
resultado_um = (numero_um * 2) * (numero_dois / 2)
print(resultado_um)

print(f'A soma do triplo do primeiro ({numero_um}) com o terceiro ({numero_tres})')
resultado_dois = (numero_um * 3) + numero_tres
print(resultado_dois)

print(f'O terceiro ({numero_tres}) elevado ao cubo')
resultado_tres = numero_tres ** 3
print(resultado_tres)
