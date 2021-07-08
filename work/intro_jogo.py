from work.adivinhacao_jogo import Adivinhacao

class Intro:

    def __init__(self):
        self._iniciar()

    def _iniciar(self):
        print('''
        ********************************
        ******** Escolha o jogo ********
        ********************************
        ''')

        cont = 's'
        while cont == 's':
            print('''
            Escolha qual jogo você quer jogar: 
            Adivinhação - [1]   Forca - [2]
            ''')
            jogar = int(input("Digite a sua opção: \n"))

            if jogar == 1:
                return Adivinhacao()
            elif jogar ==2:
                pass
            cont = str(input("Deseja jogar novamente? [s/n]: "))
            while cont not in 'sn':
                cont = str(input("Deseja jogar novamente? [s/n]: "))
            if cont == 'n':
                print("Obrigado por jogar!")

if __name__ == "__main__":
    i = Intro()

