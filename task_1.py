# 1. Гистограмма
'''
Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных зашифрованных посланиях употребляются чаще других. 
Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении. 
Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

[Формат ввода]
Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы, цифры, знаки препинания («.», «!», «?», «:», «-», «,», «;», «(», «)»), 
пробелы и переводы строк. Размер входного файла не превышает 10000 байт. Текст содержит хотя бы один непробельный символ. Все строки входного файла не длиннее 200 символов.
Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. 
Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. 
Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.


[Формат вывода]
Для каждого символа c кроме пробелов и переводов строк выведите столбик из символов «#», количество которых должно быть равно количеству символов c в данном тексте. 
Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. 
Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.
'''

with open('input.txt') as f_ptr: 
		string = ''.join(f_ptr.read().splitlines())
string = ''.join(string.split(' ')) 
words = {}
for i in string:
	words.setdefault(i, 0)
	words[i] += 1
max_val = max(words.values())
syms = sorted(words.keys())
for row in range(max_val, 0, -1):
	for key in syms:
		if words[key] >= row:
			print('#', end='')
		else:
			print(' ', end='')
	print()
print(''.join(syms))
