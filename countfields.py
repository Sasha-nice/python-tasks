"""
Функция fcounter(), которая первым параметром получает некоторый класс,
а остальные параметры применяет для создания экземпляра этого класса.
Функция должна возвращать 4 отсортированных списка: имена методов класса,
имена полей класса, имена методов, которые появились в экземпляре
(т. е. в классе их не было, а при создании экземпляра они появились)
и имена полей, которые появились в экземпляре (под «полями»
имеются в виду не-callable() атрибуты).
"""


def fcounter(C, *args):
    cm = list()
    for i in dir(C):
        if callable(getattr(C, i)) and i[0] != '_':
            cm.append(i)
    cf = list()
    for i in dir(C):
        if not callable(getattr(C, i)) and i[0] != '_':
            cf.append(i)
    c = C(*args)
    om = list()
    for i in dir(c):
        if callable(getattr(c, i)) and i not in cm and i[0] != '_':
            om.append(i)
    of = list()
    for i in dir(c):
        if not callable(getattr(c, i)) and i not in cf and i[0] != '_':
            of.append(i)
    return cm, cf, om, of
