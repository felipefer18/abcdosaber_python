# 1. ENTRADA DE DADOS
ganhos = float(input("Digite o valor total dos seus ganhos (R$): "))

# 2. PROCESSAMENTO (Verificando as faixas da tabela)
if ganhos <= 500.00:
    imposto = 0
    desconto = 0
    
elif ganhos <= 1500.00:
    imposto = 10
    desconto = ganhos * 0.10
    
elif ganhos <= 2500.00:
    imposto = 15
    desconto = ganhos * 0.15
    
else:
    # Se não caiu em nenhuma acima, é maior que 2500.01
    imposto = 20
    desconto = ganhos * 0.20

# Calculando o valor líquido (ganho menos o desconto)
valor_final = ganhos - desconto

# 3. SAÍDA DE DADOS
print("\n===============================================")
print("\n =========== Relatório de Imposto =============")
print("\n===============================================")

print(f"Ganhos Totais: R$ {ganhos:.2f}")
print(f"Imposto que foi aplicado: {imposto}%")
print(f"Valor que foi descontado: R$ {desconto:.2f}")
print(f"Valor líquido: R$ {valor_final:.2f}")