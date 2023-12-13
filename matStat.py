from statistics import median, variance

sample = [
    4.848, 2.896, 2.26, -0.985, 1.096, 5.162, 2.655, 2.437, 5.242, 3.461, 3.066,
    1.883, 3.825, 1.658, 1.06, 4.475, -0.217, 2.094, 1.834, 2.429, 4.285, 4.333, 1.378, 0.577,
    1.759, 0.816, 4.409, 3.157, 4.032, 5.137, 2.924, 4.108, 6.047, -0.296, 2.047, 3.438, 2.516,
    3.412, 4.349, 3.462, 2.136, 2.181, 5.722, 1.031, 2.254, 0.554, 2.202, -1.089, 5.441, 0.93
]


def find_mode(arr: list):
    counts = [arr.count(arr[i]) for i in range(len(arr))]
    for el in counts:
        if el > 1:
            return el
    else:
        return "Все значения уникальны"


max_el = max(sample)
min_el = min(sample)
sorted_sample = sorted(sample)

num_interval = 7
height = max_el - min_el
step_interval = height / num_interval

intervals = [round(min_el + i * step_interval, 4) for i in range(0, num_interval + 1)]

mode_ = find_mode(sample)
median_ = median(sample)
variance_ = variance(sample)
average_ = sum(sample) / len(sample)

print("-" * 40 + "Несортированная выборка" + "-" * 40)
for i in range(5):
    for j in range(10):
        print(round(sample[i + (i + 1) * j], 4), end="   ")
    print()

print("-" * 40 + "Сортированная выборка" + "-" * 40)
for i in range(5):
    for j in range(10):
        print(round(sorted_sample[i + (i + 1) * j], 4), end="   ")
    print()

print("-" * 120)
print(f"Мода = {mode_}")
print(f"Медиана = {median_}")
print(f"Выборочное среднее = {average_}")
print(f"Выборочная дисперсия = {variance_}")
print(f"Количество интервалов = {num_interval}")
print(f"Шаг интервала = {step_interval}")
print(f"Интервалы = {intervals}")

sample = sorted(sample)

for x in sample:
    print(str(x).replace(".", ","))
