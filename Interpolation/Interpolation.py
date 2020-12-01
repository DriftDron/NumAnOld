# Функция cos(x), узлы: (-0.6, -0.5, -0.3, -0.2, -0.1, 0), точка интерполирования: (-0.4), значеие функцции: (0.8)
import math


class Lagrange:
    def __init__(self, nodes, values):
        self.nodes = nodes
        val = values
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if j != i:
                    val[i] = val[i] / (nodes[i] - nodes[j])
        self.dividers = val


    def get_val(self, x):
        values = self.dividers
        s = 0
        for i in range(len(self.dividers)):
            k = 1
            for j in range(len(self.dividers)):
                if j != i:
                    k *= (x - self.nodes[j])
            s += values[i] * k
        return s


def f(x):
    return round(math.cos(x), 4)


def inv_fun(x):
    return round(math.acos(x), 8)


def p(x):
    return polynomial.get_val(x)


def newton_method(eps, a, b):
    num = 1000
    i = 1
    x_k = (a + b) / 2
    fx_k = p(x_k)
    derfx_k = (p(x_k + eps) - p(x_k)) / eps
    derffx_k = (p(x_k + 2 * eps) - 2 * p(x_k + eps) + p(x_k)) / eps
    if fx_k * derffx_k < 0:
        while True:
            xk_1 = x_k - fx_k / derfx_k
            if xk_1 < a or xk_1 > b:
                while xk_1 < a or xk_1 > b:
                    xk_1 = (x_k + xk_1) / 2
            if abs(x_k - xk_1) < eps or i >= num:
                return x_k
            x_k = xk_1
            i += 1


def bisect_method(val, a, b, eps):
    eps *= 10 ** (-3)

    while p(a) * p(b) > 0:
        a -= 1
        b += 1

    if p(a) - val == 0:
        return a
    if p(b) - val == 0:
        return a

    while b - a > eps:
        x_i = (a + b) / 2
        if (p(x_i) - val) * (p(a) - val) < 0:
            b = x_i
        else:
            a = x_i
    return a, b



arr1 = -0.6, -0.5, -0.3, -0.2, -0.1, 0
values = [f(arr1[i]) for i in range(len(arr1))]


polynomial = Lagrange(arr1, values)

y_0 = 0.8
a = 0
b = math.pi
eps = 10 ** (-6)


x1, x2 = bisect_method(y_0, a, b, eps)


x = newton_method(eps, x1, x2)
x1 = inv_fun(y_0)

if x * x1 < 0:
    x1 *= (-1)

print('Корень поулчившийся в результате обратного интерполирования:', x)
print('Корень получившийся с помощью обратной функции', x1)
print('Фактическая погрешность: ', abs(x1 - x))