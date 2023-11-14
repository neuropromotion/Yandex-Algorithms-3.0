'''
8. Минимальный прямоугольник
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

Формат ввода
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100). На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

Формат вывода
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.
'''
K = int(input())
cor = []
for i in range(K):
    cor.append(list(map(int, input().split())))

min_left = [cor[0][0], cor[0][1]]
max_right = [cor[0][0], cor[0][1]]



for i in range(K):
    if cor[i][0] < min_left[0]:
        min_left[0] = cor[i][0]

    if cor[i][1] < min_left[1]:
        min_left[1] = cor[i][1]

    if cor[i][0] > max_right[0]:
        max_right[0] = cor[i][0]

    if cor[i][1] > max_right[1]:
        max_right[1] = cor[i][1]


print(' '.join(list(map(str, min_left))), ' '.join(list(map(str, max_right))))