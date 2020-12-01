import math
from sympy import *
import pandas as pd
import numpy as np


def f(x):
    return round(math.cos(x) * (x ** (- 1 / 3)), 5)

def rect(a, b, n):
    h = (b - a) / (n - 1)
    t = 0
    for i in range(1, n):
        t += f(a + h / 2 + (i - 1) * h)
    return h * t

def Gauss(nodes, coefs):
    s = 0
    for i in range(len(nodes)):
        s += coefs[i] * f(nodes[i])
    return (1 / 2) * s

res = np.array([])
res = np.append(res, rect(0, 1, 2))

x_1, x_2 = 1/4, 3/4
x = symbols('x')
part_coef_1 = float(integrate((x - Rational(3, 4)) / (x ** Rational(1, 3)), (x, 0, 1)))
part_coef_2 = float(integrate((x - Rational(1, 4)) / (x ** Rational(1, 3)), (x, 0, 1)))

coef_1 = part_coef_1 / (x_1 - x_2)
coef_2 = part_coef_2 / (x_2 - x_1)

res = np.append(res, coef_1*math.cos(x_1) + coef_2*math.cos(x_2))

# вычисляем значение интеграла по формуле Гаусса с тремя узлами
a, b = 0, 1
t_i = [-sqrt(3/5), 0, sqrt(3/5)]
c_i = [5/9, 8./9, 5/9]
x_i = [1/2 * (a + b + (b-a)*t_i[i]) for i in range(len(t_i))]


res = np.append(res, Gauss(x_i, c_i))


n = 3
# вычисляем коэффициенты мю_k
m_k = np.array([(integrate((x ** k) / x ** Rational(1,3), (x, 0, 1))) for k in range(0, 2 * n)])
# найденные коэффициенты а_к
a_i = np.array([-1.41176470588, 0.50420168067, -0.03055767761])
# найденные узлы
xx = np.array([0.0758493318573316, 0.459885393074636, 0.876029980950385])
p1 = (xx[0] - xx[1]) * (xx[0] - xx[2])
part_1 = m_k[2] - m_k[1] * (xx[1] + xx[2]) + m_k[0] * xx[1] * xx[2]
A_1 = part_1 / p1

p2 = (xx[1] - xx[0]) * (xx[1] - xx[2])
part_2 = m_k[2] - m_k[1]*(xx[0] + xx[2]) + m_k[0] * xx[0] * xx[2]
A_2 = part_2 / p2

p3 = (xx[2] - xx[0]) * (xx[2] - xx[1])
part_3 = m_k[2] - m_k[1] * (xx[1] + xx[0]) + m_k[0] * xx[1] * xx[0]
A_3 = part_3 / p3
y = 1.32122
res = np.append(res, A_1 * math.cos(xx[0]) + A_2 * math.cos(xx[1]) + A_2 * math.cos(xx[2]))
errors = [abs(y - res[i]) for i in range(np.shape(res)[0])]
data = [res, errors]
columns = [
    "средние прямоугольники",
    "интерполяция с весом p(x)",
    "формула Гаусса",
    "формула типа Гаусса с треями узлами"]
indexes = [
    "Значение",
    "Погрешность"]
df = pd.DataFrame(data, index = indexes, columns=columns)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 5000)
print(df)