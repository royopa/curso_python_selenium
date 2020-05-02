# Loja de tintas
# pedir o tamanho em metros quadrados da área a ser pintada
# Considere a cobertura da tinta de 1 litro para cada 3 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que
# custam R$ 80,0. Informe ao usuário a quantidade de latas de
# tintas a serem compradas e o preço total
tamanho = input('Digite o tamanho em metros quadrados da área a ser pintada: ')
tamanho = float(tamanho)

quantidade_por_lata = 18
valor_por_lata = 80
rendimento_metros_por_litro = 3

rendimento_por_lata = quantidade_por_lata * rendimento_metros_por_litro
print(f'Cada lata de tinta dá para pintar {rendimento_por_lata} metros quadrados')

quantidade_latas_necessaria = tamanho // rendimento_por_lata

if tamanho % rendimento_por_lata > 0:
    quantidade_latas_necessaria = quantidade_latas_necessaria + 1

custo_total = quantidade_latas_necessaria * valor_por_lata

print(f'Portanto, você vai precisar de {quantidade_latas_necessaria}, que lhe custará R$ {custo_total}.')
