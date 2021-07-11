from random import randint

class ParImpar:

    def __init__(self,a=0,b=0):
        self._seu_ponto = a
        self._cpu_ponto = b
        self._par_ou_impar = self._escolha_par_ou_impar()
        self._seu_num = self._escolha_seu_num()
        self._cpu_num = randint(1,5)
        self._total = self._seu_num + self._cpu_num
        self.play()

    def _voltar_intro(self):
        print('Saindo do jogo de par ou impar.')
        from intro_jogo import Intro
        return Intro()


    def _escolha_par_ou_impar(self):
        sua_escolha = input("Escolha Par ou Impar [p/i]: ").strip().lower()[0]
        while sua_escolha not in 'pi':
            sua_escolha = input("Escolha Par ou Impar [p/i]: ").strip().lower()[0]
        return sua_escolha


    def _escolha_seu_num(self):
        try:
            seu_num = int(input("Digite um número inteiro:  "))
        except ValueError:
            print('\nEscolha somente números inteiros.\n')
            seu_num = int(input("Digite um número inteiro:  "))
        finally:
            return seu_num


    def _par(self):
        if self._total % 2 == 0:
            print(f"VOCÊ:{self._seu_num} e {self._cpu_num}:CPU")
            print("Você venceu!\n")
            self._seu_ponto += 1
        else:
            print(f"VOCÊ:{self._seu_num} e {self._cpu_num}:CPU")
            print("Você perdeu!\n")
            self._cpu_ponto += 1


    def _impar(self):
        if self._total % 2 != 0:
            print(f"VOCÊ:{self._seu_num} e {self._cpu_num}:CPU")
            print("Você venceu!\n")
            self._seu_ponto += 1
        else:
            print(f"VOCÊ:{self._seu_num} e {self._cpu_num}:CPU")
            print("Você perdeu!\n")
            self._cpu_ponto += 1


    def _vitoria(self):
        if self._seu_ponto > self._cpu_ponto:
            print(f"\nVocê foi o campeão com {self._seu_ponto} vitórias.\n")
        else:
            print(f"\nSinto muito, não foi dessa vez...\n")


    def play(self):
        if self._par_ou_impar == 'p':
            self._par()
        else:
            self._impar()

        jogar = input("Deseja jogar novamente? [s/n]: ")
        while jogar not in 'sn':
            jogar = input("Deseja jogar novamente? [s/n]: ")
        if jogar == 's':
            return ParImpar(self._seu_ponto,self._cpu_ponto)
        else:
            self._vitoria()
            self._voltar_intro()

if __name__ == "__main__":
    p = ParImpar()