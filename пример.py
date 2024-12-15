w=input('Введите валюту(BYN,RUB,EVRO):')
w=str(w)
if w=='BYN':
    def r():
        rub=28.51
        evro=0.29
        q = input('Введите сумму:')
        q = str(q)
        rub=rub*q
        evro=evro*q
        print('Сумма RUB, EVRO', rub, evro)
    r()