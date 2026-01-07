# 1. ENTRADA DE DADOS
# quantos dólares o turista tem
dolares = float(input("Digite a quantidade de dólares no cofre: US$ "))

# quanto está valendo 1 dólar hoje
cotacao = float(input("Qual a cotação do dólar hoje? R$ "))

# 2. PROCESSAMENTO
# Para converter, basta multiplicar a quantidade pela cotação
valor_em_reais = dolares * cotacao

# 3. SAÍDA DE DADOS
print("--- Conversão ---")
# O resultado formatado com 2 casas decimais
print(f"Com a cotação de {cotacao}, seus US$ {dolares:.2f} valem:")
print(f"R$ {valor_em_reais:.2f}")