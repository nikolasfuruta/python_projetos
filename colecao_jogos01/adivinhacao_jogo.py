from random import randint


class Adivinhacao:

    def __init__(self):
        self._dificuldade = self._iniciar()
        self._num = self._get_number()
        self._ponto = 10
        self._play()

    def _voltar_intro(self):
        print('Saindo do jogo de adivinhação.')
        from intro_jogo import Intro
        return Intro()


    def _iniciar(self):

        print('''
*********************************
Bem vindo ao jogo de adivinhação!
Tente descobrir qual o número que
o computador está pensando!!
*********************************
        
Escolha um nível de dificuldade:
[0] - Sair do jogo
[1] - Fácil
[2] - Médio
[3] - Difícil
        ''')
        escolha = int(input("Digite sua escolha: "))
        while escolha not in [0,1,2,3]:
            escolha = int(input("Digite sua escolha: "))
        if escolha == 0:
            self._voltar_intro()
        return escolha


    def _get_number(self):
        if self._dificuldade == 1:
            print("Estou pensando em um número inteiro entre 1 ao 20.")
            return randint(1, 21)
        elif self._dificuldade == 2:
            print("Estou pensando em um número inteiro entre 1 ao 50.")
            return randint(1, 51)
        elif self._dificuldade == 3:
            print("Estou pensando em um número inteiro entre 1 ao 100.")
            return randint(1, 101)


    def _get_guess(self):
        if self._dificuldade == 1:
            palpite = int(input("Digite o seu palpite: "))
            while palpite not in range(0, 20):
                print("Você está pensando em um número fora dos limites das regras.")
                palpite = int(input("Digite o seu palpite: "))
            return palpite

        elif self._dificuldade == 2:
            palpite = int(input("Digite o seu palpite: "))
            while palpite not in range(0, 50):
                print("Você está pensando em um número fora dos limites das regras.")
                palpite = int(input("Digite o seu palpite: "))
            return palpite

        elif self._dificuldade == 3:
            palpite = int(input("Digite o seu palpite: "))
            while palpite not in range(0, 100):
                palpite = int(input("Digite o seu palpite: "))
            return palpite


    def _avaliar(self,guess):
        if guess == 0:
            return False
        else:
            if guess < self._num:
                print("Ainda não, o número que você escolheu é menor do que o número que pensei.\n")
                self._ponto -= 1
                return True
            elif guess > self._num:
                print("O número que você escolheu é maior do que o número que pensei.\n")
                self._ponto -= 1
                return True
            else:
                print(f"Parabéns, você acertou!!! O número é o {guess}")
                print(f"Sua pontuação foi de {self._ponto}")
                return False


    def _play(self):
        cont = True
        while cont:
            guess = self._get_guess()
            cont = self._avaliar(guess)
        if self._ponto == 0:
            print(f'Você zerou a sua potuação.')
            print('GAMEOVER')
        jogar = str(input("Deseja jogar novamente? [s/n]: "))
        while jogar not in 'sn':
            jogar = str(input("Deseja jogar novamente? [s/n]: "))
        if jogar == 's':
            return Adivinhacao()
        else:
            self._voltar_intro()

if __name__ == "__main__":
    a = Adivinhacao()







