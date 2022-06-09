from Key import Key
from Rsa import Rsa


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
    dlugosc_klucza = 15
    stala_do_blokow = 8
    dlugosc_bloku = int(input("Podaj długość bloku: "))
    # dlugosc_bloku = 1
    text = 'Ala ma kota a kot ma ale'

    e, d, n = gen_key(dlugosc_klucza)
    print(e,n)

    rsa = Rsa(stala_do_blokow)
    lista = rsa.convert_text_to_list(text,dlugosc_bloku)

    encode, encode_txt = rsa.encode(e, n, lista)
    decode, decode_txt = rsa.decode(d, n, encode)

    with open('dane.txt', 'w') as f:
        f.write(f'Klucz publiczny: ({e},{n})\n'
                f'Klucz prywatny: ({d},{n})\n\n'
                f'Oryginalna wiadomosc: {text}\n'
                f'Dlugosc blokow: {dlugosc_bloku}\n'
                f'Zaszyfrowana wiadomosc: {encode_txt}\n'
                f'Odszyfrowana wiadomosc: {decode_txt}')
