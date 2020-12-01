#(y + 0.1) ** 2 + x ** 2 = 0.2
#x - y ** 2 = 0.37731
import sympy as sp
import pandas as pd
from math import sqrt


def Newton_method(xk, yk, eps, kmax, f, g, dfx, dfy, dgx, dgy):
    k = 0
    xx, yy, differ, val_f, val_g = [], [], [], [], []
    while True:

        xx.append(xk)
        yy.append(yk)
        val_f.append(f(xk, yk))
        val_g.append(g(xk, yk))

        D = dfx(xk, yk) * dgy(yk) - dgx(xk) * dfy(xk, yk)
        DX = f(xk, yk) * dgy(yk) - g(xk, yk) * dfy(xk, yk)
        DY = dfx(xk, yk) * g(xk, yk) - dgx(xk) * f(xk, yk)

        xk_1 = xk - DX / D
        yk_1 = yk - DY / D

        if k == 0:
            differ.append(' ')
        else:
            norma = sqrt((xx[k] - xx[k-1])**2 + (yy[k] - yy[k-1])**2)
            differ.append(norma)
            if norma < eps or k >= kmax:
                val = [xk, yk]
                break

        xk = xk_1
        yk = yk_1
        k += 1

    data = xx, yy, differ, val_f, val_g
    columns = [
        "x_k",
        "y_k",
        "norma",
        "f(x_k, y_k)",
        "g(x_k, y_k)"
    ]
    df = pd.DataFrame(data, columns).T
    df.columns.name = "k"
    return df, val

x, y = sp.symbols('x y')
plt1 = sp.plot_implicit(sp.Eq((y + 0.1) ** 2 + x ** 2 - 0.2, 0), (x, -0.7, 0.7), (y, -0.7, 0.7), show=False)
plt2 = sp.plot_implicit(sp.Eq(x - y ** 2 - 0.37731, 0), (x, -1, 1), (y, -1, 1), show=False)
plt1.extend(plt2)
plt1.show()
#(y + 0.1) ** 2 + x ** 2 = 0.2
#x - y ** 2 = 0.37731
f = lambda x, y: (y + 0.1) ** 2 + x ** 2 - 0.2
g = lambda x, y: x - y ** 2 - 0.37731
df_x = lambda x, y: 2 * x
df_y = lambda x, y: 2 * y + 0.2
dg_x = lambda x : 1
dg_y = lambda y: - 2 * y

eps = 0.00001
x_0, y_0 = 0.39, 0.1
num = 5
table_1, value_1 = Newton_method(x_0, y_0, eps, num, f, g, df_x, df_y, dg_x, dg_y)
print("Полученное приближенное решение = ", value_1)
print(table_1)

x_0, y_0 = 0.42 , -0.22
num = 5
table_2, value_2 = Newton_method(x_0, y_0, eps, num, f, g, df_x, df_y, dg_x, dg_y)
print("Полученное приближенное решение = ", value_2)
print(table_2)