from random import choice

class Forca:

    def __init__(self):
        self._erro = 0
        self._secret = self._get_secret_word()
        self._base = self._iniciar()
        self._past_letter = []
        self._play()

    def _voltar_intro(self):
        print('Saindo do jogo da Forca.')
        from work.intro_jogo import Intro #importar o arquivo intro
        return Intro()


    def _get_secret_word(self):
        with open('tiwords.txt',encoding='utf-8') as file:
            words = [line.rstrip() for line in file]
            return choice(words)


    def _iniciar(self):
        print('''
*********************************
*** Bem vindo ao jogo da Forca! ***
*********************************\n''')
        base = ['_' for i in range(len(self._secret))]
        return base


    def _visualizar(self):
        visual = ''.join(self._base)
        print(visual)


    def _avaliar(self,escolha):
        if escolha in self._secret and escolha not in self._past_letter:
            for i in range(len(self._secret)):
                if escolha == self._secret[i]:
                    self._base[i] = escolha
                    self._past_letter.append(escolha)
        else:
            print("Você errou")
            self._erro += 1


    def _ganhar_perder(self):
        if self._base == list(self._secret):
            print(f"Você acertou! A palavra é {self._visualizar()}")
            return False
        if self._erro == len(self._secret):
            print(f"Tentativas esgotadas. A palavra era {self._secret}")
            return False
        else:
            print(f"Restam {int(len(self._secret)) - self._erro} tentativas\n")
            return True



    def _play(self):
        cont = True
        while cont:
            self._visualizar()

            escolha = input("Escolha uma letra: ")
            while not escolha.isalpha():
                escolha = input("Escolha uma letra: ")

            self._avaliar(escolha)
            cont = self._ganhar_perder()

        jogar = input("Deseja jogar novamente? [s/n]:  ")
        while jogar not in 'sn':
            jogar = input("Deseja jogar novamente? [s/n]:  ")
        if jogar == 's':
            return Forca()
        else:
            self._voltar_intro()

if __name__ == "__main__":
    a = Forca()