import random

numero_secreto = random.randint(1, 100)
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    elif tentativas > 7:
        print(f"Infelizmente, você excedeu o número máximo de tentativas. O número secreto era {numero_secreto}.")
        break
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break

if tentativas <= 7:
    print("Excelente! Você é um(a) adivinhador(a) talentoso(a)!")
else:
    print("Boa tentativa! Continue praticando para melhorar suas habilidades de adivinhação.")