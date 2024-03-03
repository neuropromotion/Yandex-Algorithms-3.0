'''
18. Дек с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных deque для целых чисел.  Напишите программу, содержащую описание дека и моделирующую работу дека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push_front n
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back n
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front, pop_back, front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления деком, по одной на строке.

Формат вывода
Требуется вывести протокол работы дека, по одному сообщению на строке
'''

import sys, time
class Dequeue:
    class Node:
        value = None
        next_node = None
        prev_node = None

        def __init__(self, value):
            self.value = value
    head = None
    tail = None
    size = None
    def __init__(self):
        self.size = 0
    def push_front(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node
        self.size += 1
        print("ok")

    def push_back(self, value):
        node = self.Node(value)
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node
        self.size += 1
        print("ok")
    
    def front(self):
        if self.head == None:
            print("error")
            return
        print(self.head.value)
    
    def back(self):
        if self.tail == None:
            print("error")
            return
        print(self.tail.value)

    def pop_front(self):
        if self.head == None:
            print("error")
            return
        print(self.head.value)
        self.head = self.head.next_node
        if self.head != None:
            self.head.prev_node = None
        else:
            self.tail = None
        self.size -= 1

    def pop_back(self):
        if self.tail == None:
            print("error")
            return
        print(self.tail.value)
        self.tail = self.tail.prev_node
        if self.tail != None:
            self.tail.next_node = None
        else:
            self.head = None
        self.size -= 1
    
    def size_of_dequeue(self):
        print(self.size)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0 
        print("ok")

    def exit_(self):
        print("bye")
        sys.exit(0)


lst = Dequeue()
while True:
    str_list = input().split(' ')
    if len(str_list) > 1:
        if str_list[0] == "push_front":
            lst.push_front(int(str_list[1]))
        elif str_list[0] == "push_back":
            lst.push_back(int(str_list[1]))
    else:
        if str_list[0] == 'front':
            lst.front()
        elif str_list[0] == 'back':
            lst.back()
        elif 'exit' in str_list[0]:
            lst.exit_()
        elif 'clear' in str_list[0]:
            lst.clear()
        elif 'size' in str_list[0]:
            lst.size_of_dequeue() 
        elif 'pop_front' in str_list[0]:
            lst.pop_front()
        elif 'pop_back' in str_list[0]:
            lst.pop_back()
