import random

class Key:
    def __init__(self, n):
        self.stepik = n
        random.seed(1)


    def isPrime(self, n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        pierw = int(n ** 0.5) + 1
        for dzielnik in range(3, pierw, 2):
            if n % dzielnik == 0:
                return False
        return True

    def losuj_liczbe(self):
        while True:
            liczba = random.randint(pow(2, self.stepik - 1), pow(2, self.stepik))
            if self.isPrime(liczba):
                return liczba
