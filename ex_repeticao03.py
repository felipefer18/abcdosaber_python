# Inicializamos as variáveis de controle
soma_positivos = 0  # Isso é um ACUMULADOR (guarda a soma)
qtd_negativos = 0    # Isso é um CONTADOR (conta quantas vezes algo ocorre)

# 1. INÍCIO DO DADOS (Repetir 50 vezes)
for i in range(2):
    # Pedimos o número (usamos i+1 para mostrar "1º valor", "2º valor"...)
    valor = int(input(f"Digite o {i+1}º valor inteiro: "))
    
    # 2. PROCESSAMENTO (Condicionais)
    if valor > 0:
        # Se for positivo, adicionamos o valor à nossa soma
        soma_positivos = soma_positivos + valor
        
    elif valor < 0:
        # Se for negativo, aumentamos a contagem em 1
        qtd_negativos = qtd_negativos + 1

# 3. SAÍDA DE DADOS
print("\n ====== Resultado Final ====== ")
print(f"A soma dos valores positivos é: {soma_positivos}")
print(f"A quantidade de valores negativos é: {qtd_negativos}")