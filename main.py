from data import data
import random as rd
import time
import os


class hangman:

    def __init__(self):
        # traigo las palabras y con el módulo  random se elige una al azar
        self.words = data[0]
        self.word = self.words[rd.randint(0, 9)]
        self.mayus = self.word.upper()
        self.corretLetter = ""
        self.allLetters = ""
        self.nAttempts = 1
        # Para limpiar la pantalla.
        self.clearConsole = lambda: os.system(
            'cls' if os.name in ('nt', 'dos') else 'clear')

    # Muestro un saludo y las instrucciones previamente guardadas en un documento csv.
    def printInstructions(self):
        import csv

        print(data[4])
        with open("instructions.csv", "r", encoding="utf-8") as file:
            csv.reader = csv.DictReader(file)
            for line in file:
                print(line)

        input()
        self.clearConsole()

    def playGame(self):  # Bucle principal del juego.
        while self.nAttempts < 5:
            self.clearConsole()

            result = ""
            for letter in self.mayus:
                if letter in self.corretLetter:
                    result += letter
                else:
                    result += "_"

            print(data[2])
            print("              {}" .format("ADIVINAME"))
            print("              {}" .format(result))
            print(data[3])

            if self.nAttempts > 2:
                ready = str.upper((input("Ya sabes la palabra? YES/NOT: ")))
                if ready == "YES":
                    go = str.upper(input("Cuál es la palabra ? : "))
                    if go == self.mayus:
                        print(data[1])
                        print("Muy bien, has adivinado la palabra")
                        break
                    else:
                        print(data[5])
                        print(
                            "Has fallado y por tu culpa Stiven ha muerto, la palabra era " + self.mayus)
                        break
                elif ready == "NOT":
                    pass
                elif ready != "YES" and "NOT":
                    print("Su entrada no es valida, porfavor elija entre YES y NOT")
                    print(ready)

            attempt = str(input("Que letra falta ? : ").upper())

            if attempt in self.allLetters:
                print("Ya usaste esa letra")
                time.sleep(1)
                self.nAttempts -= 1
            else:
                pass

            if attempt not in self.mayus:
                self.nAttempts += 1
                self.allLetters += attempt
                if len(attempt) > 1:
                    print("Porfavor ingrese una sola letra")
                    time.sleep(1)
                else:
                    pass
            else:
                self.corretLetter += attempt
                self.allLetters += attempt

            if result == self.mayus:
                print("has ganado")
                break
            else:
                pass
        else:
            print(data[5])
            print(
                "Has agotado tus posibilidades y Stiven ha muerto, la palabra era " + self.mayus)


game = hangman()
game.printInstructions()
game.playGame()
