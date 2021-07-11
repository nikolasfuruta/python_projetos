from adivinhacao_jogo import Adivinhacao
from forca_jogo import Forca
from par_impar import ParImpar

class Intro:

    def __init__(self):
        self._iniciar()

    def _iniciar(self):
        print('''
********************************
******** Escolha o jogo ********
********************************
        ''')

        while True:
            print('''
Escolha qual jogo você quer jogar: 
Sair - [0]  Adivinhação - [1]   Forca - [2]  Par ou Impar - [3]
            ''')
            jogar = int(input("Digite a sua opção: "))
            while jogar not in [0,1,2,3]:
                print('Escolha somente as opções disponíveis.')
                jogar = int(input("Digite a sua opção: "))

            if jogar == 0:
                print("Obrigado por jogar!")
                break
            elif jogar == 1: return Adivinhacao()
            elif jogar == 2: return Forca()
            elif jogar == 3: return ParImpar()


if __name__ == "__main__":
    i = Intro()

