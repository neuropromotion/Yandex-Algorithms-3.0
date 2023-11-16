'''
19. Хипуй
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполнении команды Extract в структуре находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
'''

class Heap:
    arr = None
    size = None 
    def __init__(self):
        self.size = 0
        self.arr = []
    
    def insert(self, val):
        self.arr.append(val)
        self.size += 1 
        val_pos = self.size-1
        relative_pos = (val_pos-1)//2 
        while self.arr[val_pos] > self.arr[relative_pos] and val_pos > 0:
            self.arr[val_pos], self.arr[relative_pos] = self.arr[relative_pos], self.arr[val_pos]
            val_pos = relative_pos
            relative_pos = (val_pos-1)//2
    
    def extract(self):
        extracted_val = self.arr[0]
        self.arr[0] = self.arr[-1]
        pos = 0
        pos_left_child = 2*pos + 1
        pos_right_child = 2*pos + 2
        while (pos_right_child < len(self.arr)):
            pos_max_child = pos_left_child
            if self.arr[pos_right_child] > self.arr[pos_left_child]:
                pos_max_child = pos_right_child
            if self.arr[pos] < self.arr[pos_max_child]:
                self.arr[pos], self.arr[pos_max_child] = self.arr[pos_max_child], self.arr[pos] 
                pos = pos_max_child
                pos_left_child = 2*pos + 1
                pos_right_child = 2*pos + 2
            else:
                break
        self.arr.pop()
        self.size -= 1
        print(extracted_val)
        return

heap = Heap()

with open('input.txt') as ptr:
    N = int(ptr.readline())
    for i in range(N):
        line = ptr.readline()
        order = list(map(int, line.split(' ')))
        if len(order) > 1:
            heap.insert(order[1])
            continue
        heap.extract()
'''
N = int(input())
for i in range(N):
    order = list(map(int, input().split(' ')))
    if len(order) > 1:
        heap.insert(order[1])
        continue
    heap.extract()

'''



