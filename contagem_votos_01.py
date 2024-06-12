# Inicializamos as variáveis contadoras para cada tipo de voto
votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_branco = 0

# Início do laço para ler os votos de 20 eleitores
for i in range(0, 20):
    voto = int(input('Informe seu voto: '))  # Solicita o voto do eleitor
    if voto == 1:
        votos_candidato1 += 1  # Incrementa votos para o candidato 1
    elif voto == 2:
        votos_candidato2 += 1  # Incrementa votos para o candidato 2
    elif voto == 3:
        votos_candidato3 += 1  # Incrementa votos para o candidato 3
    elif voto == 4:
        votos_candidato4 += 1  # Incrementa votos para o candidato 4
    elif voto == 5:
        votos_nulos += 1  # Incrementa votos nulos
    elif voto == 6:
        votos_branco += 1  # Incrementa votos em branco
    else:
        print("Voto inválido.")  # Informa sobre voto inválido

# Exibição do resultado da contagem de votos
print(f'Votos candidato 1: {votos_candidato1}')
print(f'Votos candidato 2: {votos_candidato2}')
print(f'Votos candidato 3: {votos_candidato3}')
print(f'Votos candidato 4: {votos_candidato4}')
print(f'Votos nulos: {votos_nulos}')
print(f'Votos em branco: {votos_branco}')

# Cálculo e exibição do percentual de votos nulos e em branco
print(f'Percentual de votos nulos: {(votos_nulos / 20 * 100):.2f}%')
print(f'Percentual de votos em branco: {(votos_branco / 20 * 100):.2f}%')

