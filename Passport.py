"""fio - фамилия имя оичество,
   old - дата рождения от (14 до 120) от 0 до 9
   ps - паспортные данные (**** ******), числа
   weigh - вес в килограммах от (20 и выше)"""
from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзиклмнопрстуфхцчшщьыъэюяй"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.veryfy_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.weight = weight
        self.ps = ps

    @classmethod
    def veryfy_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("fio должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("неверный формат ввода")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("в fio должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("в fio можно использовать только буквы")

    @classmethod
    def veryfy_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("возраст должен быть цифрой")

    @classmethod
    def veryfy_weight(cls, w):
        if type(w) != float or w < 20.0:
            raise TypeError("вес должен быть 20 килограмм и выше")

    @classmethod
    def veryfy_ps(cls, ps):
        if type(ps) !=str:
            raise TypeError("паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("некорректный ввод номера паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("паспорт должен быть цифровой")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.veryfy_weight(weight)
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.veryfy_ps(ps)
        self.__ps = ps


w = Person("малюшицкий александр александрович", 109,"1234 123456",34.9)
w.old=200
print(w.old)

print(w.__dict__)
