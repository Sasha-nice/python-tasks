"""
Параметрический декоратор TypeCheck(последовательность_типов, тип_результата),
который бросает исключение TypeError при вызове функции со следующим сообщением:

-"Type of argument Номер is not Тип", если не совпадает тип позиционного
параметра функции и соответствующий ему по порядку тип в
последовательности_типов
-"Type of argument Имя is not Тип", если не совпадает тип именного
параметра функции  и соответствующий ему тип в последовательности_типов.
Типы именованных параметров перечислены в конце последовательности_типов
в порядке их описания в def …
"Type of result is not Тип", если тип возвращённого функцией значения
не совпадает с типом_результата
"Function функция must have число arguments" — если количество переданных функции
параметров (включая переданные по умолчанию) не соответствует длине
последовательности_типов
Сначала проверяются параметры в порядке описания в функции, затем вызывается функция,
после чего проеряется результат. Ислкючение возникает при первом несовпадении типа.
"""


def TypeCheck(posl, res):

    posl = list(posl)

    def decor(fun):
        def dfun(*argc, **argv):
            if len(posl) != len(argc) + len(argv):
                raise TypeError(
                    f'Function {fun.__name__} must have {len(posl)} arguments'
                )
            for i in range(len(argc)):
                if type(argc[i]) != posl[i]:
                    raise TypeError(
                        f'Type of argument {i + 1} is not {(posl[i])} '
                    )
            cur = 0
            for i in argv:
                if type(argv[i]) != posl[cur + len(argc)]:
                    raise TypeError(
                        f" Type of argument '{i}' is not {posl[cur]}"
                    )
                cur += 1
            if type(fun(*argc, **argv)) != res:
                raise TypeError(
                    f'Type of result is not {res}'
                )
            return fun(*argc, **argv)
        return(dfun)
    return decor