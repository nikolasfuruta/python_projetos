from random import choice

class Forca:

    def __init__(self):
        self._secret = self._get_secret_word()
        self._base = self._iniciar(self._secret)
        self._play(self._secret,self._base)

    def _voltar_intro(self):
        print('Saindo do jogo da Forca.')
        from work.intro_jogo import Intro #importar o arquivo intro
        return Intro()


    def _get_secret_word(self):
        with open('tiwords.txt',encoding='utf-8') as file:
            words = [line.rstrip() for line in file]
            return choice(words)


    def _iniciar(self,secret):
        print('''
*********************************
*** Bem vindo ao jogo da Forca! ***
*********************************\n''')
        base = ['_' for i in range(len(secret))]
        return base


    def _visualizar(self,base):
        visual = ''.join(base)
        print(visual)


    def _avaliar(self,escolha,secret,base,erro):
        if escolha in secret:
            for i in range(len(secret)):
                if escolha == secret[i]:
                    base[i] = escolha
            return erro
        else:
            print("Você errou")
            erro += 1
            return erro


    def _ganhar_perder(self,secret,base,erro):
        if base == list(secret):
            print(f"Você acertou! A palavra é {self._visualizar(base)}")
            return False
        if erro == len(secret):
            print(f"Tentativas esgotadas. A palavra era {secret}")
            return False
        else:
            print(f"Restam {int(len(secret)) - erro} tentativas\n")
            return True



    def _play(self,secret,base):
        erro = 0
        cont = True
        while cont:
            self._visualizar(base)

            escolha = input("Escolha uma letra: ")
            while not escolha.isalpha():
                escolha = input("Escolha uma letra: ")

            erro = self._avaliar(escolha,secret,base,erro)
            cont = self._ganhar_perder(secret,base,erro)

        jogar = input("Deseja jogar novamente? [s/n]:  ")
        while jogar not in 'sn':
            jogar = input("Deseja jogar novamente? [s/n]:  ")
        if jogar == 's':
            return Forca()
        else:
            self._voltar_intro()

if __name__ == "__main__":
    a = Forca()