#2. Красивая строка
'''
Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

[Формат ввода]
В первой строке записано одно целое число k (0 ≤ k ≤ 109) 
Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 105). Строчка S состоит только из маленьких латинских букв.

[Формат вывода]
Выведите одно число — максимально возможную красоту строчки, которую можно получить.
'''
k = int(input())
string = input()
leng = len(string)
alpha = 'abcdefghljklmnopqrstuvwxyz'
count = maxim = first = last = 0
t = k
for word in alpha: 
	while last < leng and first < leng:   
		while last < leng and string[last] == word:
			last += 1
			count += 1
			maxim = maxim if maxim > count else count
		else:
			if t != 0:
				t -= 1  
				count += 1 
				maxim = maxim if maxim > count else count
				last += 1
			else:
				while string[first] == word: 
					count -= 1
					first += 1
				else:
					t += 1
					count -= 1
					first += 1  
	t = k
	first = last = count = 0

print(maxim)
