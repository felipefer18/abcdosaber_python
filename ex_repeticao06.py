# Inicializamos os contadores para cada faixa
menos_que_dez = 0
entre_dez_e_quinze = 0
acima_de_quinze = 0

# Perguntamos quantos alunos participaram da pesquisa
total_alunos = int(input("Quantos alunos foram entrevistados para essa pesquisa? "))

# 1. ENTRADA E CLASSIFICAÇÃO
for i in range(total_alunos):
    vezes = int(input(f"Quantas vezes o {i+1}º aluno usou o restaurante? "))
    
    if vezes < 10:
        menos_que_dez += 1
    elif 10 <= vezes <= 15:
        entre_dez_e_quinze += 1
    else:
        acima_de_quinze += 1

# 2. CÁLCULO DOS PERCENTUAIS
# Fórmula: (parte / total) * 100
perc_menor_10 = (menos_que_dez / total_alunos) * 100
perc_10_a_15 = (entre_dez_e_quinze / total_alunos) * 100
perc_maior_15 = (acima_de_quinze / total_alunos) * 100

# 3. SAÍDA DE DADOS
print("\n ====== Resultado da Pesquisa ======")
print(f"Menos que 10 vezes: {perc_menor_10:.1f}%")
print(f"Entre 10 e 15 vezes: {perc_10_a_15:.1f}%")
print(f"Acima de 15 vezes: {perc_maior_15:.1f}%")