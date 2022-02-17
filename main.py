import math

#KLASA I METODY MAGICZNE
class Ulamek:
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

    def __add__(self, drugi):
        result = Ulamek(int(self.liczba1) + int(drugi.liczba1), int(self.liczba2))
        result.shorten()
        return result

    def __sub__(self, drugi):
        result = Ulamek(int(self.liczba1) - int(drugi.liczba1), int(self.liczba2))
        result.shorten()
        return result

    def __mul__(self, drugi):
        result = Ulamek(int(self.liczba1) * int(drugi.liczba1), int(self.liczba2) * int(drugi.liczba2))
        result.shorten()
        return result

    def __truediv__(self, drugi):
        result = Ulamek(int(self.liczba1) * int(drugi.liczba2), int(self.liczba2) * int(drugi.liczba1))
        result.shorten()
        return result

    def shorten(self):
        nwd = math.gcd(self.liczba1, self.liczba2)
        self.liczba1 //= nwd
        self.liczba2 //= nwd

    def __str__(self):
        return str(self.liczba1) + "/" + str(self.liczba2)

class Calc:
    def pobieranie(self):

        #POBIERANIE KILKU WIERSZY
        contents = []
        bladlist = []
        while True:
            try:
                dzialanie = input()
            except EOFError:
                break
            contents.append(dzialanie)

        #SPRAWDZANIE CZY PODANO POPRAWNE DZIALANIE
        for i in range(len(contents)):
            try:
                liczba1, znak, liczba2 = contents[i].split(" ")
            except:
                print("BLAD")
                bladlist.append(i)
                exit()

        #SPRAWDZANIE CZY ZMIENNA NIE JEST PUSTA
        for i in range(len(contents)):
            if i not in bladlist:
                if liczba1 == "" or liczba2 == "":
                    print("BLAD")
                    exit()

        # SPRAWDZENIE CZY OPERATOR JEST PRAWIDLOWY
        if znak in ("+", "-", "*", ":"):
            pass
        else:
            print("BLAD")
            exit()

        #SPRAWDZANIE CZY PIERWSZA LICZBA TO ULAMEK
        try:
            licznik1, mianownik1 = liczba1.split("/")
        except:
            liczba1 = [liczba1, "/1"]
            liczba1 = "".join(liczba1)
            licznik1, mianownik1 = liczba1.split("/")

        #SPRAWDZANIE CZY DRUGA LICZBA TO ULAMEK
        try:
            licznik2, mianownik2 = liczba2.split("/")
        except:
            liczba2 = [liczba2, "/1"]
            liczba2 = "".join(liczba2)
            licznik2, mianownik2 = liczba2.split("/")

        #SPRAWDZENIE CZY ULAMKI NIE MAJA 0 W MIANOWNIKU
        if int(mianownik1) == 0 or int(mianownik2) == 0:
            print("BLAD")
            exit()

        ulamek1 = Ulamek(licznik1, mianownik1)
        ulamek2 = Ulamek(licznik2, mianownik2)

        #DZIALANIA
        if (znak == "+" or znak == "-"):
            if (mianownik1 != mianownik2):
                licznik11 = int(licznik1) * int(mianownik2)
                mianownik11 = int(mianownik1) * int(mianownik2)
                licznik22 = int(licznik2) * int(mianownik1)
                mianownik22 = int(mianownik2) * int(mianownik1)
                ulamek1 = Ulamek(licznik11, mianownik11)
                ulamek2 = Ulamek(licznik22, mianownik22)
            if (znak == "+"):
                addition = ulamek1 + ulamek2
                print(addition)
            if (znak == "-"):
                subtraction = ulamek1 - ulamek2
                print(subtraction)
        if (znak == "*"):
            multiplication = ulamek1 * ulamek2
            print(multiplication)
        if (znak == ":"):
            truediv = ulamek1 / ulamek2
            print(truediv)

if __name__ == "__main__":
    calc = Calc()
    calc.pobieranie()