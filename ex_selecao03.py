# 1. ENTRADA DE DADOS
# Usamos float para que o programa aceite números quebrados (ex: -1.5 ou 2.5)
numero = float(input("Digite um número: "))

# 2. PROCESSAMENTO E SAÍDA (Tudo junto usando Condicionais)
if numero > 0:
    # Se o número for maior que zero
    print(f"O número {numero} é POSITIVO.")

elif numero < 0:
    # Se o número não for maior que zero, mas for menor que zero
    print(f"O número {numero} é NEGATIVO.")

else:
    # Se não for maior que zero e nem menor que zero, só pode ser zero!
    print("O número é ZERO.")