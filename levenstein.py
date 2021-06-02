"""
Функция для подсчёта расстояние Левейнштейна между строками
"""


def levenstein(a, b):


	def f(a, b):
    	return a != b


    def rec_leven(m, n):
        if m == 0:
            return n
        if n == 0:
            return m
        return min(rec_leven(m, n - 1) + 1, rec_leven(m - 1, n) + 1, rec_leven(m - 1, n - 1) + f(a[m - 1], b[n - 1]))


    return rec_leven(len(a), len(b))

