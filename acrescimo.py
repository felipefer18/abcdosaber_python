# 1. ENTRADA DE DADOS
preco_custo = float(input("Digite o preço de custo do produto: R$ "))
percentual_lucro = float(input("Digite a porcentagem de acréscimo (ex: 30 para 30%): "))

# 2. PROCESSAMENTO
# Calculamos o valor do acréscimo
valor_acrescimo = preco_custo * (percentual_lucro / 100)

# Somamos o acréscimo ao custo original para ter o preço de venda
preco_venda = preco_custo + valor_acrescimo

# 3. SAÍDA DE DADOS
print("-" * 20)
print(f"Resumo da Venda:")
print(f"Custo: R$ {preco_custo:.2f}")
print(f"Lucro ({percentual_lucro}%): R$ {valor_acrescimo:.2f}")
print(f"Preço Final de Venda: R$ {preco_venda:.2f}")