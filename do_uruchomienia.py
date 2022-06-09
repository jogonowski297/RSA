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

class Rsa:
    def __init__(self,stala,dl_boku):
        self.stala = stala
        self.dl_boku = dl_boku
        self.rozbite = []

    def convert_to_ascii(self, text):
        return [ord(i) for i in list(text)]

    def convert_from_ascii(self,lista):
        text = ""
        for i in lista:
            text += chr(i[0])
        return text

    def sum(self, lista, stala):
        liczba = 0
        for i in range(len(lista)):
            liczba += (lista[i]*pow(stala,i))
        return [int(liczba)]

    def base256toint(self,L):
        total = 0
        L.reverse()
        for i in range(len(L)):
            total = total + L[i]*(pow(self.stala,i))
        return total

    def base_expansion(self, n,b):
        q = n
        digit_list = []
        while q != 0:
            digit_list.append(q % b)
            q = q // b
        digit_list.reverse()
        return digit_list

    def inttostring(self, M):
        L = self.base_expansion(M,self.stala)
        message = ''
        for d in L:
            message += chr(d)
        return message

    def convert_text_to_list(self, text, dl_bloku):
        if dl_bloku == 1:
            return [self.convert_to_ascii(i) for i in text]

        test = []
        for i in range(0, len(self.convert_to_ascii(text)), dl_bloku):
            test.append(self.base256toint(self.convert_to_ascii(text)[i:i + dl_bloku]))

        return [[i] for i in test]

    def encode(self, e, n, lista):
        encode = [[pow(i[0],e,n)] for i in lista]

        encode_txt = ""
        for i in encode:
            encode_txt += f'{i[0]} '

        return encode, encode_txt

    def decode(self, d, n, lista):
        decode = [[pow(i[0],d,n)] for i in lista]

        decode_txt = ""
        for i in decode:
            decode_txt += str(i[0])

        return decode, decode_txt


def get_from_file_encode(file):
    tab = []
    with open(file, 'r') as f:
        rsa = f.read()
    for i in rsa.split(' '):
        tab.append([int(i)])
    return tab

def get_from_file_decode(file):
    with open(file, 'r', encoding="utf-8") as f:
        rsa = f.read()
    return rsa


def gen_key(n_stepik):
    def find_d(x, y):
        def xyz(a, b):
            if b == 0:
                return (1, 0)
            (q, r) = (a // b, a % b)
            (s, t) = xyz(b, r)
            return (t, s - (q * t))

        inv = xyz(x, y)[0]
        if inv < 1: inv += y
        return inv

    key = Key(n_stepik)

    p = key.losuj_liczbe()
    q = key.losuj_liczbe()

    euler = (p - 1) * (q - 1)
    n = p * q
    e = key.losuj_liczbe()

    d = find_d(e, euler)

    return e, d, n


if __name__ == "__main__":
    zaszyfrowane = get_from_file_encode("zaszyfrowane")
    odszyfrowane = get_from_file_decode("odszyfrowane.txt")
    stala_do_blokow = pow(2, 8)
    dlugosc_klucza = 12
    # dlugosc_bloku = 1
    dlugosc_bloku = int(input("Podaj dlugosc bloku: "))
    e, d, n = gen_key(dlugosc_klucza)
    rsa = Rsa(stala_do_blokow, dlugosc_bloku)

    chose = input("Co chcesz zrobic?\n"
                  "1) Odszyfrowac z pliku 'zaszyfrowane.txt'\n"
                  "2) Zaszyfrowac z pliku 'odszyfrowane.txt'\n"
                  "3) Zapisz wygenerowane klucze do pliku 'rsa_key.txt'")

    if chose == '1':
        decode, decode_txt = rsa.decode(d, n, zaszyfrowane)
        print("Odszyfrowana wiadomość: ")
        for i in decode:
            print(rsa.inttostring(i[0]).encode("utf-8").decode(), end='')
    elif chose == '2':
        lista = rsa.convert_text_to_list(odszyfrowane, dlugosc_bloku)
        encode, encode_txt = rsa.encode(e, n, lista)
        print("Zaszyfrowana wiadomość:")
        print(encode_txt)
    elif chose == '3':
        with open("rsa_key.txt", 'w') as f:
            f.write(f'Klucz publiczny: ({e}, {n})\n'
                    f'Klucz prywatny: ({d}, {n})')

