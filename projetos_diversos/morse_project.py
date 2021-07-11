class Morse:
    __morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
             'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
             'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
             'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
             '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.'}

    def __init__(self):
        self._frase = self._qual_a_frase()
        self._tranduzir = self._traduzir_frase()
        self._printar()

    def _qual_a_frase(self):
        frase = str(input("Digite a sua frase: "))
        return frase.lower().strip().split()

    def _traduzir_frase(self):
        new = []
        for word in self._frase:
            for letter in word:
                if letter in self.__morse.keys():
                    new.append(self.__morse[letter]) #retorna o valor
                new.append(' ') #espaço entre letras
            new.append('  ') #espaço entre palavras
        return new

    def _printar(self):
        res = ''.join(self._tranduzir)
        print(res)

if __name__ == "__main__":
    morse_code = Morse()