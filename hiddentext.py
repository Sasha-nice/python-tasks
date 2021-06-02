"""
Ввести две строки и проверить, содержится ли вторая в первой,
с учётом того, что символы второй строки могут находиться в
первой на некотором равном расстоянии друг от друга. Вывести YES или NO.
"""


str1 = input()
str2 = input()
f = False
copy = str1
while str2[0] in copy:
    for i in range(len(str1) - 1):
        if copy[copy.index(str2[0])::i + 1][:len(str2)] == str2:
            f = True
            break
    copy = copy[copy.index(str2[0]) + 1:]
if f:
    print('YES')
else:
    print('NO')
