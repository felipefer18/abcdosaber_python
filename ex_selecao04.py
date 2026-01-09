# 1. ENTRADA DE DADOS
numeros= [  ]

print("\n===============================================")
print("\n============ Jogo dos Algoritmos ==============")
print("\nVamos ver quais números são divisiveis por 2 e por 3")
print("\n===============================================")

for i in range(4):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

print("\n ===== Resultados =====")

# 2. PROCESSAMENTO E SAÍDA
encontrou = False # Variável para avisar se achamos algum número

for n in numeros: 

    # n % 2 == 0 significa "se o resto da divisão de n por 2 for zero"
    if (n % 2 == 0) and (n % 3 == 0):
        print(f"O número {n} é divisível por 2 e 3.")
        encontrou = True

if not encontrou:
    print("Nenhum dos números processados é divisível por 2 e 3 simultaneamente.")