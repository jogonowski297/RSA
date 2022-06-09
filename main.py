from Key import Key
from Rsa import Rsa

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
    # print(n)
    # while len(str(n)) + len(str(e)) != n_stepik:
    #     print(e)
    #     e = key.losuj_liczbe()

    d = find_d(e, euler)

    return e, d, n


if __name__ == "__main__":
    zaszyfrowane = get_from_file_encode("zaszyfrowane.txt")
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

