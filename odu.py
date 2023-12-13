from matplotlib import pyplot as plt

x0: float = 1
y0: float = 1
xn: float = 3
h: float = 0.5


def differential_equation(x, y):
    return x + y + 2


def euler_method(func, y0, x0, xn, h):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < xn:
        x_n = x_values[-1]
        y_n = y_values[-1]
        y_n1 = y_n + h * func(x_n, y_n)

        x_values.append(x_n + h)
        y_values.append(y_n1)

    return x_values, y_values


def modified_euler_method(f, x0, y0, xn, h):
    values = []

    x = x0
    y = y0

    while x <= xn:
        values.append((x, y))
        y_pred = y + h * f(x, y)
        y = y + h / 2 * (f(x, y) + f(x + h, y_pred))
        x += h

    return values


ecoX_1: list = [2.32, 2.33, 2.38, 2.41, 2.44, 2.48, 2.51, 2.55, 2.58, 2.60]
ecoY_1: list = [427, 430, 440, 444, 448, 455, 460, 462, 465, 466]

ecoX_2: list = [0.5, 1, 2, 3, 4, 5, 6, 6.5, 7, 7.5]
ecoY_2: list = [1000, 1001, 1004, 1010, 1020, 1030, 1050, 1060, 1070, 1080]

engX_1: list = [10, 20, 40, 60, 90, 110, 120, 130, 140, 150]
engY_1: list = [1.5, 1.8, 3, 3.9, 4.8, 5.5, 5.7, 7, 8.1, 9.4]

engX_2: list = [1.2, 2, 3, 4, 5.1, 5.9, 7, 8, 9, 9.8]
engY_2: list = [2.3, 3.71, 4.81, 5.9, 6.3, 6.25, 5.87, 4.82, 3.7, 2.29]


def runge_kutta(f, x0, y0, xn, h):
    result = []
    x = x0
    y = y0

    while x <= xn:
        result.append((x, y))
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

    return result


def plot_euler_method():
    x_values, y_values = euler_method(differential_equation, x0, y0, xn, h)

    plt.plot(x_values, y_values, label='Euler Method')
    plt.scatter(x_values, y_values, color='red')  # Scatter plot for points
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Euler Method')
    plt.legend()
    plt.show()


def plot_modified_euler_method():
    result_modified_euler = modified_euler_method(differential_equation, x0, y0, xn, h)
    x_values, y_values = zip(*result_modified_euler)

    plt.plot(x_values, y_values, label='Modified Euler Method')
    plt.scatter(x_values, y_values, color='red')  # Scatter plot for points
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Modified Euler Method')
    plt.legend()
    plt.show()


def plot_runge_kutta():
    solution = runge_kutta(differential_equation, x0, y0, xn, h)
    x_values, y_values = zip(*solution)

    plt.plot(x_values, y_values, label='Runge-Kutta Method')
    plt.scatter(x_values, y_values, color='red')  # Scatter plot for points
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Runge-Kutta Method')
    plt.legend()
    plt.show()