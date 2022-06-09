class Rsa:
    def __init__(self,stala):
        self.stala = stala
        pass

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
        return [liczba]

    def convert_text_to_list(self, text, dl_bloku):
        if dl_bloku == 1:
            print([self.convert_to_ascii(i) for i in text])
            return [self.convert_to_ascii(i) for i in text]

        list_word = []
        for i in range(0, len(self.convert_to_ascii(text)), dl_bloku):
            list_word.append(self.sum(self.convert_to_ascii(text)[i:i + dl_bloku],self.stala))

        print(list_word)
        return list_word

    def encode(self, e, n, lista):
        encode = [[pow(i[0],e,n)] for i in lista]

        encode_txt = ""
        for i in encode:
            encode_txt += str(i[0])

        # print(encode)
        print("Zaszyfrowana: ",encode_txt)
        return encode, encode_txt

    def decode(self, d, n, lista):
        decode = [[pow(i[0],d,n)] for i in lista]

        decode_txt = ""
        for i in decode:
            decode_txt += str(i[0])

        # print(decode)
        print("Odszyfrowana: ",decode_txt)
        return decode, decode_txt
