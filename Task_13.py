'''
13. Постфиксная запись
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.
Формат ввода
В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *. Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.
Формат вывода
Необходимо вывести значение записанного выражения.
'''
sequence = input().split(' ') 
size = len(sequence)
class Stack: 
	def __init__(self):
		self.stack = []
	def add(self, num):
		self.stack.append(int(num))
	def calc(self, operator):
		if operator == '+':
			self.stack[-2] = self.stack[-1] + self.stack[-2]
			self.stack.pop()
		elif operator == '*':
			self.stack[-2] = self.stack[-1] * self.stack[-2]
			self.stack.pop()
		elif operator == '-':
			self.stack[-2] = self.stack[-2] - self.stack[-1]
			self.stack.pop() 
stack = Stack()

ind = True
i = 0
while (ind):
	if sequence[i].isnumeric():
		stack.add(sequence[i])
	else:
		stack.calc(sequence[i])
	i += 1
	ind = True if i < size else False



'''ind = True 
while (ind):
	if sequence[0].isnumeric():  
		stack.add(sequence[0])
		sequence.pop(0)
	else:
		stack.calc(sequence[0])
		sequence.pop(0) 
	ind = True if sequence else False'''

print(stack.stack[0])
