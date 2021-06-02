"""
Надёжный калькулятор
Написать программу — калькулятор с переменными и обработкой ошибок.
Программа построчно вводит команды калькулятора, и если надо,
выводит результат их выполнения или ошибку.

Пробелы в строках игнорируются
Команда, начинающаяся на '#' — комментарий, такие команды игнорируются
Команда вида "Идентификатор = выражение" задаёт переменную Идентификатор
(именование как в Python)
Если слева от "=" стоит не идентификатор, выводится "Assignment error";
всё, что справа, игнорируется
Команда вида "выражение" выводит значение выражения.
Выражение — это арифметическое выражение, состоящее из
- целых чисел
- уже определённых идентификаторов
- круглых скобок
- действий +, -, *, /, % и унарных + и -.
- - Деление целочисленное
Любое другое выражение приводит к выводу ошибки "Syntax error"
Если выражение нельзя вычислить, потому что в нём встречаются неопределённые
переменные, выводится ошибка "Name error"
"""
import re

d = {}
s = input()
g = 0
while s:
    f = 0
    w = re.search(r'^[0-9]+[a-zA-Z_]+', s)
    if w:
        print(w.group())
        print('Syntax error')
        s = input()
        continue
    if s[0] == '#':
        s = input()
        continue
    if '**' in s:
        print('Syntax error')
        s = input()
        continue
    if '.' in s:
        print('Syntax error')
        s = input()
        continue
    if r'//' in s:
        print('Syntax error')
        s = input()
        continue
    if s.count('=') > 1:
        print('Syntax error')
        s = input()
        continue
    w = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', s)
    if w is not None:
        s1 = str()
        for i in w:
            if (len(s) > s.index(i) + len(i)) and s[s.index(i) + len(i)] == '(':
                print('Syntax error')
                f = 1
                break
            s1 = s1 + s[:s.index(i)] + '_c_' + s[s.index(i):s.index(i) + len(i)]
            s = s[s.index(i) + len(i):]
        s = s1 + s
    if f == 1:
        s = input()
        continue
    s1 = str()
    for i in range(len(s)):
        if s[i] == r'/':
            s1 = s1 + r'//'
            continue
        s1 = s1 + s[i]
    s = s1
    if '=' in s:
        l = re.split(r'\s*=\s*', s)
        try:
            w = re.search(r'^[a-zA-Z_]\w*', l[0]).group()
        except AttributeError:
            print('Assignment error')
            s = input()
            continue
        if l[0] in d:
            try:
                print(eval(int(l[1]), d))
            except ValueError:
                print('Syntax error')
                s = input()
                continue
        else:
            d[l[0]] = (eval(l[1], d))
        s = input()
        continue

    try:
        print(eval(s, d))
    except NameError:
        print('Name error')
    except TypeError:
        print('Syntax error')
    except ZeroDivisionError:
        print('Runtime error')
    finally:
        s = input()
