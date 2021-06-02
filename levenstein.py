"""
Функция для подсчёта расстояние Левейнштейна между строками
"""


def levenstein(a, b):


	def f(a, b):
    	return a != b

    cache = {}
    def rec_leven(m, n):
    	if (m, n) in cache:
    		return cache[(m, n)]
        if m == 0:
        	cache[(m, n)] = n
            return n
        if n == 0:
        	cache[(m, n)] = m
            return m
        cur = min(rec_leven(m, n - 1) + 1, rec_leven(m - 1, n) + 1, rec_leven(m - 1, n - 1) + f(a[m - 1], b[n - 1]))
        cache[(m, n)] = cur
        return cur


    return rec_leven(len(a), len(b))

