from random import randint


class Adivinhacao:

    def __init__(self):
        self._dificuldade = self._iniciar()
        self._num = self._get_number(self._dificuldade)
        self._play(self._dificuldade,self._num)

    def _voltar_intro(self):
        print('Saindo do jogo de adivinhação.')
        from work.intro_jogo import Intro
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


    def _get_number(self,dificuldade):
        if dificuldade == 1:
            print("Estou pensando em um número inteiro entre 1 ao 20.")
            return randint(1, 21)
        elif dificuldade == 2:
            print("Estou pensando em um número inteiro entre 1 ao 50.")
            return randint(1, 51)
        elif dificuldade == 3:
            print("Estou pensando em um número inteiro entre 1 ao 100.")
            return randint(1, 101)


    def _get_guess(self,dificuldade):
        print('Digite zero para sair do jogo\n')
        if dificuldade == 1:
            guess = int(input("Digite o seu palpite: "))
            while guess not in range(0, 20):
                print("Você está pensando em um número fora dos limites das regras.")
                guess = int(input("Digite o seu palpite: "))
            return guess

        elif dificuldade == 2:
            guess = int(input("Digite o seu palpite: "))
            while guess not in range(0, 50):
                print("Você está pensando em um número fora dos limites das regras.")
                guess = int(input("Digite o seu palpite: "))
            return guess

        elif dificuldade == 3:
            guess = int(input("Digite o seu palpite: "))
            while guess not in range(0, 100):
                print("Você está pensando em um número fora dos limites das regras.")
                guess = int(input("Digite o seu palpite: "))
            return guess


    def _play(self,dificuldade,num):
        ponto = 10
        while ponto > 0:
            guess = self._get_guess(dificuldade)
            if guess == 0: break

            else:
                if guess < num:
                    print("Ainda não, o número que você escolheu é menor do que o número que pensei.\n")
                    ponto -= 1
                elif guess > num:
                    print("O número que você escolheu é maior do que o número que pensei.\n")
                    ponto -= 1
                    continue
                else:
                    print(f"Parabéns, você acertou!!! O número é o {guess}")
                    print(f"Sua pontuação foi de {ponto}")
                break

        if ponto == 0:
            print(f'Você zerou a sua potuação.')
            print('GAMEOVER')

        cont = str(input("Deseja jogar novamente? [s/n]: "))
        while cont not in 'sn':
            cont = str(input("Deseja jogar novamente? [s/n]: "))
        if cont == 's':
            self._iniciar()
        else:
            print('Saindo do jogo de adivinhação.')
            self._voltar_intro()

if __name__ == "__main__":
    a = Adivinhacao()







