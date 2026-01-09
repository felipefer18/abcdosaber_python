# 1. ENTRADA DE DADOS
valor_compra = float(input("Digite o valor total da compra: R$ "))

# 2. PROCESSAMENTO (Tomada de decisão)
if valor_compra >= 5000.00:
    # Se for 5000 ou mais, desconto de 20%
    porcentagem = 20
    desconto = valor_compra * 0.20
else:
    # Caso contrário (menor que 5000), desconto de 15%
    porcentagem = 15
    desconto = valor_compra * 0.15

# Cálculo do valor final
valor_final = valor_compra - desconto

# 3. SAÍDA DE DADOS
print("-" * 30)
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {porcentagem}% (- R$ {desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")