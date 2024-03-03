'''
16. Очередь с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы. 

Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из очереди первый элемент. Программа должна вывести его значение.

front
Программа должна вывести значение первого элемента, не удаляя его из очереди.

size
Программа должна вывести количество элементов в очереди.

clear
Программа должна очистить очередь и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления очередью, по одной на строке

Формат вывода
Требуется вывести протокол работы очереди, по одному сообщению на строке
'''

import sys
class Queue:
	def __init__(self):
		self.queue = []
	def push(self, val):
		self.queue.append(val)
		print('ok')
	def pop(self):
		if self.size():
			print(self.queue.pop(0))
		else:
			print('error')
	def front(self):
		if self.size():
			print(self.queue[0])
		else:
			print('error')
	def back(self):
		if self.size():
			print(self.queue[-1])
		else:
			print('error')
	def clear(self):
		self.queue = []
		print('ok')
	def exit(self):
		print('bye')
		sys.exit()
	def size(self):
		return len(self.queue)
	def size_(self):
		print(len(self.queue))
    
queue = Queue()
while True:
	order = input().split(' ')
	if len(order) > 1:
		queue.push(int(order[1]))
	else:
		if order[0] == 'pop':
			queue.pop()
		elif order[0] == 'front':
			queue.front()
		elif order[0] == 'back':
			queue.back()
		elif order[0] == 'clear':
			queue.clear()
		elif order[0] == 'exit':
			queue.exit()
		elif order[0] == 'size':
			queue.size_()
