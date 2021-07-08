from random import randint

def introducao():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

def dificuldade():
    print("Escolha um nível de dificuldade:")
    print("Fim - [0]  Fácil - [1]  Médio - [2]  Difícil - [3]")
    return int(input("Nível: "))

def get_magic_num(nivel):
    if nivel == 1:
        print("Estou pensando em um número inteiro entre 1 ao 20.")
        return randint(1, 21)
    elif nivel == 2:
        print("Estou pensando em um número inteiro entre 1 ao 50.")
        return randint(1, 51)
    elif nivel == 3:
        print("Estou pensando em um número inteiro entre 1 ao 100.")
        return randint(1, 101)

def game(nivel,magic_num):
    ponto = 100
    while True:
        guess = int(input("Qual é o número? "))
        try:
            if nivel == 1:
                if guess > 21:
                    raise ValueError
            elif nivel == 2:
                if guess > 51:
                    raise ValueError
            elif nivel == 3:
                if guess > 101:
                    raise ValueError
        except:
            print("O número escolhido não está de acordo com as regras do jogo!\n")
            continue
        else:
            if guess == 0:
                break
            elif guess < magic_num:
                print("Ainda não, o número escolhido é menor do que o número que pensei.\n")
                ponto -= 1
                continue
            elif guess > magic_num:
                print("O número escolhido é maior do que o número que pensei.\n")
                ponto -= 1
                continue
            else:
                print(f"Parabéns, você acertou!!! O número é o {guess}")
                print(f"Sua pontuação foi de {ponto}")
            break

def play_again():
    flag = str(input("\nDeseja jogar novamente? [s/n]- "))
    if flag == "n":
        print("Obrigado por jogar!")
        return False
    else:
        return True


def jogar():
    introducao()
    play = True
    while play:
        nivel = dificuldade()
        print('')
        if nivel == 0:
            print("Obrigado por jogar!")
            break
        else:
            magic_num = get_magic_num(nivel)
        game(nivel,magic_num)
        play = play_again()


if __name__ == "__main__":
    jogar()