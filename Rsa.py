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
            # liczba += str(lista[i])
            liczba += (lista[i]*pow(stala,i))
        return [int(liczba)]
    ###################################################

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


    ###################################################
    def convert_text_to_list(self, text, dl_bloku):
        if dl_bloku == 1:
            # print([self.convert_to_ascii(i) for i in text])
            return [self.convert_to_ascii(i) for i in text]

        # list_word = []
        test = []
        for i in range(0, len(self.convert_to_ascii(text)), dl_bloku):
            test.append(self.base256toint(self.convert_to_ascii(text)[i:i + dl_bloku]))
            # list_word.append(self.sum(self.convert_to_ascii(text)[i:i + dl_bloku],self.stala))

        # print(f'test: {test}')
        # # print(f'list_word: {list_word}')
        return [[i] for i in test]

    def encode(self, e, n, lista):
        encode = [[pow(i[0],e,n)] for i in lista]

        encode_txt = ""
        for i in encode:
            encode_txt += f'{i[0]} '

        # print(encode)
        # print(encode_txt)
        # print("Zaszyfrowana: ",encode_txt)
        return encode, encode_txt

    def decode(self, d, n, lista):
        decode = [[pow(i[0],d,n)] for i in lista]

        decode_txt = ""
        for i in decode:
            decode_txt += str(i[0])

        # print(f'decoded: {decode}\n'
        #       f'{decode_txt}')
        # for i in decode:
        #     print(self.inttostring(i[0]), end='')

        # self.div_sum(decode)
        # print("Odszyfrowana: ",decode_txt)
        return decode, decode_txt
