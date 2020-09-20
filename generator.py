import random

f1 = open('DARK_TOWERS1.txt', 'r')

class generator:
    def __init__(self):
        # словарь где ключ - первое слово, значение - словарь, где ключ - второе слово, значение - кол-во повторений этого слова после первого
        self._D = {} #protected переменная

    def fit(self, s):
        s = s.split(' ')
        # creating dict that we need
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]
            if a in self._D.keys():
                if b in self._D[a].keys():
                    self._D[a][b] += 1
                else:
                    self._D[a][b] = 1
            else:
                self._D[a] = {b: 1}

    def get_new_word(self, a):
        b = random.choices(list(self._D[a].keys()),
                           list(self._D[a].values()))  # неравновероятный выбор следующего слова
        return b[0]

    def predict(self, s):
        s1 = list(s.split())
        a = s1[-1]  # начальное слово
        endi = ['.', '!', '?']
        while True:  # генерация следующих слов пока не встретится конец предложения
            try:
                b = self.get_new_word(a) #на случай если слово ни разу не встречалось и продолжить мы не можем
            except:
                return 'This is my first time seeing word %s, so I can\'t coninue.' % a
            s1.append(b)
            if b in endi:
                break
            a = b
        return ' '.join(s1)

#main programm
s = f1.read()   #читаем текст
print('Введите начало предложения на английском в нижнем регистре:')
sin = input()
gen = generator()
gen.fit(s)
print(gen.predict(sin))
