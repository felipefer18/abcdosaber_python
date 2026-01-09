# Inicializamos as variáveis de controle
soma = 0  # 
quantidade = 0    
numeros = []
continua = 1

# 1. INÍCIO DO DADOS (Repetir 50 vezes)
while continua !=0:
    numero = int(input("Digite um valor inteiro: "))
    numeros.append(numero)

    continua = int(input("Deseja continuar? (1-Sim / 2-Não):"))


#2 PROCESSAMENTO
    for numero in numeros:
        if numero >= 0:
            soma = soma + numero   

# 3. SAÍDA DE DADOS
print("\n ====== Resultado Final ====== ")
print(f"A soma dos valores positivos é: {soma_positivos}")
print(f"A quantidade de valores negativos é: {qtd_negativos}")