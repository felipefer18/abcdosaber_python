# entrada de dados:
produto = input('Digite o nome do produto: ')
valor = float(input("Digite o valor do produto: "))

# processamento
desconto = valor * 0.09
novo_valor = valor - desconto

#saida de dados
print(f"O produto {produto} com o valor original de R${valor:.2f} com desconto de 9% fica por R$ {novo_valor:.2f}.") 
