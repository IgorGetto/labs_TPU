import math


class Unit:
    def __init__(self, name, value, code):
        # имя объекта, значение вероятности, код объекта
        self.name = name
        self.value = value
        self.code = code


# алгоритм Шеннона-Фано - принимает список объектов класса, возвращает тот же список, но с присвоенными кодами
def make_shannon_fano(probability):
    summ = 0
    index = 0
    for i in probability:
        summ += i.value  # получили сумму вероятностей

    group = summ / 2

    group1 = []
    group2 = []
    # and abs(group - index - i.value) < abs(group - index)
    for i in probability:
        if index < group:
            index += i.value
            if index > group and abs(group - index) > abs(group - index + i.value):
                i.code += '0'
                group2.append(i)
            else:
                i.code += '1'
                group1.append(i)
        # elif abs(group - index) > abs(group - index - i.value):
        #     index = group
        #     i.code -= '1'
        #     i.code += '0'
        #     group1.remove(i)
        #     group2.append(i)
        else:
            i.code += '0'
            group2.append(i)


            # рекурсия
    if len(group1) != 1:
        make_shannon_fano(group1)
    if len(group2) != 1:
        make_shannon_fano(group2)

    return probability


def entropy_shannon(probability):
    entropy = 0
    for i in probability.values():
        entropy += i*math.log(1/i, 2)
    return entropy


def cost(probability):
    val = 0
    for i in probability:
        val += len(i.code)*i.value
    return val


z = {"z1": 0.26, "z2": 0.19, "z3": 0.14, "z4": 0.11,
     "z5": 0.1, "z6": 0.08, "z7": 0.07, "z8": 0.05}

# для каждого элемента создаем соответствующий объект класса
index = 1
data = []
for i in z:
    name = Unit(i, z[i], '')
    data.append(name)

# сортируем по полю value в порядке убывания
data = sorted(data, key=lambda x: x.value, reverse=True)

# применяем алгоритм
data = make_shannon_fano(data)

# выводим коды букв
for i in data:
    print(i.name, i.value, i.code)

print('энтропия по Шеннону:', entropy_shannon(z))
print('средняя длина кодовой комбинации', cost(data))

'''
Задание используя алгоритм Шеннона-Фано, провести эффективное кодирование ансамбля из букв своей фамилии:
'''

last_name = {"Г": 0.2, "Е": 0.2, "Т": 0.4, "О": 0.2}
# для каждого элемента создаем соответствующий объект класса
index = 1
data = []
for i in last_name:
    name = Unit(i, last_name[i], '')
    data.append(name)

# сортируем по полю value в порядке убывания
data = sorted(data, key=lambda x: x.value, reverse=True)

# применяем алгоритм
data = make_shannon_fano(data)

# выводим коды букв
for i in data:
    print(i.name, i.value, i.code)

print('энтропия по Шеннону:', entropy_shannon(last_name))
print('средняя длина кодовой комбинации', cost(data))

z2 = dict(
    z1z1=0.49,
    z1z2=0.14,
    z2z1=0.14,
    z1z3=0.07,
    z3z1=0.07,
    z2z2=0.04,
    z2z3=0.02,
    z3z2=0.02,
    z3z3=0.01
)

# для каждого элемента создаем соответствующий объект класса
index = 1
data = []
for i in z2:
    name = Unit(i, z2[i], '')
    data.append(name)

# сортируем по полю value в порядке убывания
data = sorted(data, key=lambda x: x.value, reverse=True)

# применяем алгоритм
data = make_shannon_fano(data)

# выводим коды букв
for i in data:
    print(i.name, i.value, i.code)

print('энтропия по Шеннону:', entropy_shannon(z2))
print('средняя длина кодовой комбинации', cost(data))



z3_FIO = dict(
    o=0.18,
    i=0.136364,
    t=0.136364,
    v=0.09,
    g=0.09,
    r=0.09,
    z_=0.09,
    k=0.0454545,
    e=0.0454545,
    q=0.0454545,
    ch=0.0454545
)

# для каждого элемента создаем соответствующий объект класса
index = 1
data = []
for i in z3_FIO:
    name = Unit(i, z3_FIO[i], '')
    data.append(name)

# сортируем по полю value в порядке убывания
data = sorted(data, key=lambda x: x.value, reverse=True)

# применяем алгоритм
data = make_shannon_fano(data)

# выводим коды букв
for i in data:
    print(i.name, i.value, i.code)

print('энтропия по Шеннону:', entropy_shannon(z2))
print('средняя длина кодовой комбинации', cost(data))