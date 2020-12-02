import math
from math import exp
import pandas as pd
from sympy import *
# вычисляем значение функции в точке х
def f(x):
    return round(math.e**(3*x), 5)


# вычисляем производную k порядка в точке х
def der(x, k):
    return round((3**k)*f(x), 5)


# числ. дифф. 1 порядка, погрешность O(h)
def num_diff_1_1(arr, h):
    values_1_1 = []
    for i in range(len(arr)):
        if i == len(arr) - 1:
            values_1_1.append(' ')
        else:
            values_1_1.append(round((arr[i + 1] - arr[i]) / h, 5))
    return values_1_1


# числ. дифф. 1 порядка, погрешность O(h^2)
def num_diff_1_2(arr, h):
    values_1_2 = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            values_1_2.append(' ')
        else:
            values_1_2.append(round((arr[i + 1] - arr[i - 1]) / 2 * h, 5))
    return values_1_2


# числ. дифф. 2 порядка, погрешность O(h^2)
def num_diff_2(arr, h):
    values_2 = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            values_2.append(' ')
        else:
            values_2.append(round((arr[i + 1] - 2 * arr[i] + arr[i - 1]) / h ** 2, 5))
    return values_2


# вычисляем погрешность O(h) = f' - f'(h)~
def err_1(ders, difs):
    errors_1 = []
    for i in range(len(difs)):
        if i == len(difs) - 1:
            errors_1.append(' ')
        else:
            errors_1.append(ders[i] - difs[i])
    return errors_1

def lol(x):
    return 1 + 3.4986 * x + 6.12 * x*(x-1) + 7.13667 * x*(x-0.1)*(x-0.2) + 6.25 * x*(x-0.1)*(x-0.2)*(x-0.3) + 4.325 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4) + 2.70833 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5) + 0.81343 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6) + 1.63721 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7) - 2.01246 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7)*(x-0.8) + 4.30036 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7)*(x-0.8)*(x-0.9)


# вычисляем погрешность O(h^2)
def err_2(ders, difs):
    errors_2 = []
    for i in range(len(difs)):
        if i == 0 or i == len(difs) - 1:
            errors_2.append(' ')
        else:
            errors_2.append(ders[i] - difs[i])
    return errors_2

print('Полином')
h = 0.1
a = 0
b = 1

xx = [] # массив узлов
for i in range(int(b / h + 1)):
    xx.append(round(a + i * h, 1))

values = []
derr_1 = []
derr_2 = []
for x in xx:
    values.append(f(x))
    derr_1.append(der(x, 1))
    derr_2.append(der(x, 2))

diffs_1_1 = num_diff_1_1(values, h)
diffs_1_2 = num_diff_1_2(values, h)
diffs_2 = num_diff_2(values, h)

errors_1_1 = err_1(derr_1, diffs_1_1)
errors_1_2 = err_2(derr_1, diffs_1_2)
errors_2 = err_2(derr_2, diffs_2)

data = [values, derr_1, diffs_1_1, errors_1_1, diffs_1_2, errors_1_2, derr_2, diffs_2, errors_2]
indexes = [
    "f(x)",
    "f'(x)",
    "f'(x),  O(h)",
    "O(h)",
    "f'(x),  O(h^2)",
    "O(h^2)",
    "f''(x)",
    "f''(x),  O(h^2)",
    "O(h^2)"
    ]
y1 = xx
y2 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y3 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y4 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y5 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y6 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y7 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y8 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y9 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y10 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
y11 = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,]
for i in range(10):
    y1[i] = round((values[i+1] - values[i]) / (xx[i+1] - xx[i]),5)
for i in range(10):
    y2[i] = round((y1[i+1] - y1[i]) / (0.2),5)
for i in range(10):
    y3[i] = round((y2[i+1] - y2[i]) / (0.3),5)
for i in range(10):
    y4[i] = round((y3[i+1] - y3[i]) / (0.4),5)
for i in range(10):
    y5[i] = round((y4[i+1] - y4[i]) / (0.5),5)
for i in range(10):
    y6[i] = round((y5[i+1] - y5[i]) / (0.6),5)
for i in range(10):
    y7[i] = round((y6[i+1] - y6[i]) / (0.7),5)
for i in range(10):
    y8[i] = round((y7[i+1] - y7[i]) / (0.8),5)
for i in range(10):
    y9[i] = round((y8[i+1] - y8[i]) / (0.9),5)
for i in range(10):
    y10[i] = round((y9[i+1] - y9[i]) / (1.0),5)

print("P(x) = 1 +",y1[0],'* x +',y2[0],'* x(x-1) +',y3[0],'* x(x-0.1)(x-0.2) +',y4[0],'* x(x-0.1)(x-0.2)(x-0.3) +',y5[0],'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4) +\n+',y6[0],'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4)(x-0.5) +',y7[0],'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4)(x-0.5)(x-0.6) +\n+',y8[0],'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4)(x-0.5)(x-0.6)(x-0.7) -',abs(y9[0]),'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4)(x-0.5)(x-0.6)(x-0.7)(x-0.8) +\n+',y10[0],'* x(x-0.1)(x-0.2)(x-0.3)(x-0.4)(x-0.5)(x-0.6)(x-0.7)(x-0.8)(x-0.9)')
x = symbols('x')
print(diff(1 + 3.4986 * x + 6.12 * x*(x-1) + 7.13667 * x*(x-0.1)*(x-0.2) + 6.25 * x*(x-0.1)*(x-0.2)*(x-0.3) + 4.325 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4) + 2.70833 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5) + 0.81343 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6) + 1.63721 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7) - 2.01246 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7)*(x-0.8) + 4.30036 * x*(x-0.1)*(x-0.2)*(x-0.3)*(x-0.4)*(x-0.5)*(x-0.6)*(x-0.7)*(x-0.8)*(x-0.9),x,2))
