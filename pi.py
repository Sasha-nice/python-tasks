"""
Бесконечный генератор PiGen(), вычисляющий Decimal представление
числа Пи c 9999 знаками после запятой (всего 10000)
по алгоритму Чудновских. На каждой итерации PiGen()
возвращает значение для очередного k.
"""


def PiGen():
    from decimal import getcontext
    from decimal import Decimal
    getcontext().prec = 10000
    sum = Decimal(0)
    i = 0
    con1 = 1
    con2 = 1
    con3 = 13591409
    con4 = 1
    con5 = 1
    con6 = Decimal.sqrt(Decimal(640320 * 640320 * 640320))
    con6 = 12 / con6
    param = 1
    while True:
        sum += con1 * con2 * con3 * con6 / (con4 * con5 * con5 * con5 * param)
        yield Decimal(1 / sum)
        i += 1
        con1 *= -1
        con2 *= (6 * i) * (6 * i - 1) * (6 * i - 2) * (6 * i - 3) * \
                (6 * i - 4) * (6 * i - 5)
        con3 += 545140134
        con4 *= (3 * i) * (3 * i - 1) * (3 * i - 2)
        con5 *= i
        param *= 640320 * 640320 * 640320
