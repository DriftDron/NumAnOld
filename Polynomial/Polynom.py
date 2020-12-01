import math
import pandas as pd


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
    return round(1 / (1 + x ** 2), 5)

    # вычисляем узлы
def node(k, n):
    val = math.cos(math.pi * (2 * k + 1) / (2 * (n + 1)))
    return val

    # вычисляем значение полинома
def chebishev_val(x, n):
    nodes = [node(k, n) for k in range(n + 1)]  # узлы - корни многочлена Чебышева
    values = [f(nodes[i]) for i in range(len(nodes))]  # значения функции в узлах
    polynomial = Lagrange(nodes, values)  # вычисляем делители полинома Лагранжа
    return polynomial.get_val(x)  # возвращаем значение полинома в точке х

def f(x):
    return round(1 / (1 + x ** 2), 5)

    # вычисляем значение полинома степени n в точке х
def newton_val(n, coefs, a, h):
    arr = []
    nodes = []
    for i in range(n + 1):
        nodes.append(a + h * (i - n // 2))
        arr.append(f(a + h * (i - n // 2)))
    diffs = sep_diffs(arr, nodes)
    values = [0] * (n + 1)
    k = (n // 2)
    sch = 0

    for i in range(len(diffs)):
        y = coefs[i]
        sch += 1
        y *= diffs[i][k]
        y = round(y, 5)
        if i == 0:
            values[i] = y
        else:
            values[i] = values[i - 1] + y
        if sch % 3 == 2:
            k -= 1
        return values[n]

    # разделенные разности
def sep_diffs(arr, nodes):
    RR1 = []
    for i in range(len(arr) - 1):
        val = (arr[i + 1] - arr[i])
        RR1.append(val)
    RR2 = []
    for i in range(len(arr) - 2):
        val = RR1[i + 1] - RR1[i]
        RR2.append(val)
    RR = [arr, RR1, RR2]  # будущий массив разделенных разностей

    for i in range(3, len(arr)):
        vals = []
        for j in range(len(arr) - i):
            vals.append(round((RR[i - 1][j + 1] - RR[i - 1][j]), 5))
        RR.append(vals)
    return RR

    # коэффициенты N_k для составления полинома
def coefficient(n, t):
    coefs = [0] * (n + 1)
    coefs[0] = 1
    for i in range(1, n + 1):
        y = 1
        for j in range(1, i + 1):
            y *= (t - ((-1) ** j) * (j // 2)) / j
        coefs[i] = round(y, 5)
    return coefs

x = 0.15
a, b = -1, 1
y = round(1 / (1 + x ** 2), 6)  # точное значение фукнции

n_s = [5, 10, 20]
h = 0.2
t = round((x - a) / h, 1)

coefs = [coefficient(n, t) for n in n_s]
value_1 = []  # значения полинома
for i in range(len(coefs)):
    value_1.append(newton_val(n_s[i], coefs[i], a, h))

errors_1 = [abs(y - value_1[i]) for i in range(len(value_1))]  # погрешности

value_2 = [chebishev_val(x, n) for n in n_s]
errors_2 = [abs(y - value_2[i]) for i in range(len(value_2))]

print('Точное значение функции в точке x = 0.15 :', y)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
data = [n_s, value_1, errors_1, value_2, errors_2]
indexes = [
    "n",
    "значение по равноотстоящим узлам",
    "погрешность",
    "значение по корням Чебышева",
    "погрешность"
]
df = pd.DataFrame(data, index = indexes).T
print(df)