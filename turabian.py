"""
Программа, которой на вход подаётся две строки — библиографическая ссылка B
на некоторую книгу и внутритекстовая ссылка N на эту же книгу.
Программа должна проверить, что обе ссылки синтаксически верны и
ссылаются на одну и ту же книгу. Формат ссылок — упрощённый стиль
Турабьян. Вывод программы — True, если B соответствует N,
и False — если не соответствует, или такое соответствие невозможно
определить из-за синтаксической некорректности.
"""
import re


def func(s):
    expr = re.search(r'(.+\.?)\. (.+)\. (.+): (.+), ([0-9]+)', s)
    if expr is None:
        return False
    expr = re.search(r'(.+\.?)\. (.+)\. (.+): (.+), ([0-9]+)', s).groups()
    authors = expr[0]
    title = expr[1]
    city = expr[2]
    publisher = expr[3]
    year = expr[4]
    names = list()
    cur = list()
    if len(re.split(r',\s', authors)) < 2:
        return False
    cur.append(re.split(r',\s', authors)[1])
    cur.append(re.split(r',\s', authors)[0])
    names.append(cur)
    for i in re.split(r',\s', authors)[2:]:
        names.append(i)
    if len(names) > 1:
        names[-1] = names[-1][4:]
    result = list()
    result.append(names)
    result.append(title)
    result.append(city)
    result.append(publisher)
    result.append(year)
    return result


b1 = input()
s = input()
result = func(s)
flag = True
b = re.search(r'[^0-9\. ].+[^0-9\., –]', b1).group()
if result:
    if b1[0] == b[0]:
        flag = False
    end = '(' + result[2] + ': ' + result[3] + ', ' + result[4] + ')'
    end = result[1] + ' ' + end
    end2 = end
    end1 = end
    if len(result[0]) == 1:
        end = result[0][0][0] + ' ' + result[0][0][1] + ', ' + end
        end2 = result[0][0][0] + '. ' + result[0][0][1] + ', ' + end1
    if len(result[0]) == 2:
        end = result[0][0][0] + ' ' + result[0][0][1] + ' and ' + \
              result[0][1] + ', ' + end
    if len(result[0]) == 3:
        end = result[0][0][0] + ' ' + result[0][0][1] + ', ' + \
              result[0][1] + ', and ' + result[0][2] + ', ' + end
    if len(result[0]) >= 4:
        end = result[0][0][0] + ' ' + result[0][0][1] + ' et al., ' + end
        end2 = result[0][0][0] + ' ' + result[0][0][1] + ' et al.,' + \
               re.split(r'\.', result[0][-1])[-1] + '. ' + end1
if result and (b == end or b == end2) and flag:
    print(True)
else:
    print(False)
