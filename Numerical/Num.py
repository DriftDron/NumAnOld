import math
from math import exp
import pandas as pd

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


# вычисляем погрешность O(h^2)
def err_2(ders, difs):
    errors_2 = []
    for i in range(len(difs)):
        if i == 0 or i == len(difs) - 1:
            errors_2.append(' ')
        else:
            errors_2.append(ders[i] - difs[i])
    return errors_2

print('Первый пункт')
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

df = pd.DataFrame(data, index=indexes, columns = [i for i in xx]).T
df.columns.name = 'x'
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
print(df)

print('Второй пункт')


# вычисляем значение функции в точке х
def f(x):
    return round(exp(3 * x), 5)


# вычисление точной производной
def der(x, k):
    return round((3 ** k) * f(x), 5)


# второй разностной производной второго порядка аппроксимации
def derivative(x, h):
    return round((f(x + h) - 2 * f(x) + f(x - h)) / h ** 2, 5)

x = 1 # точка вычисления
h = 0.1 # начальное значение шага
df = der(x, 2) # точное значение f''(x=1)

err = [abs(df - derivative(x, h))] # фактическая погрешность при h=0.1
i = 0
# вычисляем погрешность, пока не начнет возрастать
while True:
    i += 1
    h /= 2
    err.append(abs(df - derivative(x, h)))
    if err[i] - err[i-1] > 0:
        break
h *= 2
for er in err:
    print(er)

print('Оптимальное h = ', h)
print('Точное значение производной второго порядка = ', df)
print('Значение второй разностной  производной второго порядка аппроксимации = ', derivative(x, h) )

print('Третий пункт')
a = 1  #x_0 = 1
steps = [0.1, 0.05, 0.025, 0.0125]
xx = [] # массив узлов
for i in range(len(steps)):
    xx.append([a-steps[i], a, a+steps[i]])
# точное значение второй производной в точке х_0 = 1
y = der(a,2)

values= []  # массив значений f(x)
for j in range(len(xx)):
    arr = [f(x) for x in xx[j]]
    values.append(arr)

# считаем численное значение производных и погрешностей
diffs = [(values[i][0] - 2*values[i][1] + values[i][2])/(steps[i]**2) for i in range(len(values))]
errors = [abs(diffs[j] - y) for j in range(len(diffs))]

# печатаем таблицу погрешностей
column = ['f(x)']
data = [steps, diffs, errors ]
indexes = [
    "Шаг h",
    "Численное значение производной",
    "Погрешность"
]
df = pd.DataFrame(data, index = indexes)
print('Фактическое значение производной = ', y)
print(df)