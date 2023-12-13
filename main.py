def lagrange(x: list[float], y: list[float], x0: float) -> float | None:

    if len(x) != len(y) or len(x) == 0:
        return

    n: int = len(x)

    y0: float = 0.0

    for i in range(n):
        l: float = y[i]
        for j in range(n):
            if i != j:
                l *= (x0 - x[j]) / (x[i] - x[j])

        y0 += l

    return y0


def divided_differences(x_values: list[float], y_values: list[float]) -> list[float]:
    n = len(x_values)
    f = y_values.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            f[i] = (f[i] - f[i - 1]) / (x_values[i] - x_values[i - j])

    return f


def newton_interpolation(x_values: list[float], y_values: list[float], x: float) -> float:
    n = len(x_values)
    f = divided_differences(x_values, y_values)
    result = f[0]

    for i in range(1, n):
        term = f[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term

    return result


x: list[float] = [-1, 4, 5]
y: list[float] = [2, 1, 3]

x0_1: float = 3.0
x0_2: float = 6.0
x0_3: float = 9.0

# print(f"y({x0_1}) = {lagrange(x, y, x0_1)}")
# print(f"y({x0_2}) = {lagrange(x, y, x0_2)}")
# print(f"y({x0_3}) = {lagrange(x, y, x0_3)}")

print(f"y({x0_1}) = {newton_interpolation(x, y, x0_1)}")
print(f"y({x0_2}) = {newton_interpolation(x, y, x0_2)}")
print(f"y({x0_3}) = {newton_interpolation(x, y, x0_3)}")




# import matplotlib.pyplot as plt
# import numpy as np


def linear_approximation(x_values: list[float], y_values: list[float], x: float):
    n = len(x_values)

    mean_x = sum(x_values) / n
    mean_y = sum(y_values) / n

    a = sum((x_values[i] - mean_x) * (y_values[i] - mean_y) for i in range(n)) / sum(
        (x_values[i] - mean_x) ** 2 for i in range(n))
    b = mean_y - a * mean_x

    y_approximated = a * x + b

    return a, b, y_approximated


def quadratic_approximation(x_values: list[float], y_values: list[float], x: float):
    n = len(x_values)

    sum_x = sum(x_values)
    sum_x_squared = sum(x_i ** 2 for x_i in x_values)
    sum_y = sum(y_values)
    sum_x_y = sum(x_i * y_i for x_i, y_i in zip(x_values, y_values))

    denominator = n * sum_x_squared - sum_x ** 2
    b_numerator = n * sum_x_y - sum_x * sum_y
    c_numerator = sum_y * sum_x_squared - sum_x * sum_x_y

    a = denominator / denominator
    b = b_numerator / denominator
    c = c_numerator / denominator

    y_approximated = a * x**2 + b * x + c

    return a, b, c, y_approximated


def less_squares(x_values: list[float], y_values: list[float], x: float) -> tuple[float] or None:
    if len(y_values) != len(x_values) or len(x_values) == 0:
        return

    n: int = len(x_values)
    a: float
    b: float

    xy_sum: float = 0

    x_sum: float = 0
    y_sum: float = 0
    x_sq_sum: float = 0

    for i in range(n):
        xy_sum += x_values[i] * y_values[i]
        x_sum += x_values[i]
        y_sum += y_values[i]
        x_sq_sum += x_values[i] ** 2

    sq_sum_x: float = x_sum ** 2

    # print(f"{xy_sum} {x_sum} {y_sum} {x_sq_sum} {n}")

    a_numerator: float = n * xy_sum - x_sum * y_sum
    b_numerator: float = x_sq_sum * y_sum - x_sum * xy_sum
    denominator: float = n * x_sq_sum - sq_sum_x

    a = a_numerator / denominator
    b = b_numerator / denominator

    y_approximate = a * x + b

    return a, b, y_approximate


# #task_5
# x: list[float] = [2.32, 2.33, 2.38, 2.41, 2.44, 2.48, 2.51, 2.55, 2.58, 2.60]
# y: list[float] = [427.0, 430.0, 440.0, 444.0, 448.0, 455.0, 460.0, 462.0, 465.0, 466.0]

# x: list[float] = [2.32, 2.33, 2.38, 2.41, 2.44, 2.48, 2.51, 2.55, 2.58, 2.60]
# y: list[float] = [427.0, 430.0, 440.0, 444.0, 448.0, 455.0, 460.0, 462.0, 465.0, 466.0]


# ecoX_1: list = [2.32, 2.33, 2.38, 2.41, 2.44, 2.48, 2.51, 2.55, 2.58, 2.60]
# ecoY_1: list = [427, 430, 440, 444, 448, 455, 460, 462, 465, 466]
#
# ecoX_2: list = [0.5, 1, 2, 3, 4, 5, 6, 6.5, 7, 7.5]
# ecoY_2: list = [1000, 1001, 1004, 1010, 1020, 1030, 1050, 1060, 1070, 1080]
#
# engX_1: list = [10, 20, 40, 60, 90, 110, 120, 130, 140, 150]
# engY_1: list = [1.5, 1.8, 3, 3.9, 4.8, 5.5, 5.7, 7, 8.1, 9.4]
#
# engX_2: list = [1.2, 2, 3, 4, 5.1, 5.9, 7, 8, 9, 9.8]
# engY_2: list = [2.3, 3.71, 4.81, 5.9, 6.3, 6.25, 5.87, 4.82, 3.7, 2.29]
#
#
# ecoX0_1: float = 3.0
# ecoX0_2: float = 8.0
# engX0_1: float = 160.0
# engX0_2: float = 10.0


ecoX_1: list = [500, 520, 523, 530, 550, 555, 560, 562, 565, 570]
ecoY_1: list = [61, 66.8, 67, 69, 74, 76.7, 78, 79, 79.3, 81]

ecoX_2: list = [10,  20,  30,  40,  50,  60,  70,  80,  90,  95]
ecoY_2: list = [1000, 600, 480, 430, 415, 412, 410, 405, 400, 392]

engX_1: list = [3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5]
engY_1: list = [25, 28, 30, 32, 36, 39, 41, 44, 46, 47]

engX_2: list = [10,  20,  30,  40,  50,  60,  70,  80,  90,  95]
engY_2: list = [1000, 602, 479, 430, 416, 412, 410, 406, 400, 391]


ecoX0_1: float = 600.0
ecoX0_2: float = 100.0
engX0_1: float = 6.2
engX0_2: float = 100.0


# a, b, c, y_x = quadratic_approximation(engX_2, engY_2, engX0_2)
#
# print(f"{a = } {b = } {c = } y({engX0_2}) = {y_x}")


def plot_less_squares_approximation(x_values: list[float], y_values: list[float], volume: float = 8.0):
    a, b, costs = less_squares(x_values, y_values, volume)

    # print(f"{k = }, {b = }")
    # print(f"Затраты на производстве при {3.0} у.е равняются {costs} рублям")

    x_values_for_plot = np.linspace(min(engX_2), max(engX_2), 100)
    y_values_for_plot = a * x_values_for_plot + b




