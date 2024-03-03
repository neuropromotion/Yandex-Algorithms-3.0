'''
Калькулятор
Имеется калькулятор, который выполняет следующие операции:

умножить число X на 2;
умножить число X на 3;
прибавить к числу X единицу.
Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 106.

Формат вывода
В первой строке выходного файла выведите минимальное количество операций. Во второй строке выведите числа, последовательно получающиеся при выполнении операций. 
Первое из них должно быть равно 1, а последнее N. Если решений несколько, выведите любое.

'''

n = int(input()) 
if n == 1:
    print(0)
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 0
    prev = [0] * (n+1)
    for i in range(2, n+1):
        if i % 3 == 0 and i % 2 == 0:
            #dp[i] = min(dp[int(i/3)], dp[int(i/2)], dp[i-1]) + 1

            if (dp[int(i/3)] <= min(dp[int(i/2)], dp[i-1])): 
                dp[i] = dp[int(i/3)] + 1
                prev[i] = int(i/3)
            elif (dp[int(i/2)] <= dp[i-1]):
                dp[i] = dp[int(i/2)] + 1
                prev[i] = int(i/2)
            else:
                dp[i] = dp[i-1] + 1
                prev[i] = i-1
        elif i % 3 == 0:
            #dp[i] = min(dp[int(i/3)], dp[i-1]) + 1

            if (dp[int(i/3)] <= dp[i-1]):
                dp[i] = dp[int(i/3)] + 1
                prev[i] = int(i/3)
            else:
                dp[i] = dp[i-1] + 1
                prev[i] = i-1  
        elif i % 2 == 0:
            #dp[i] = min(dp[int(i/2)], dp[i-1]) + 1

            if (dp[int(i/2)] <= dp[i-1]):
                dp[i] = dp[int(i/2)] + 1
                prev[i] = int(i/2)
            else:
                dp[i] = dp[i-1] + 1
                prev[i] = i-1  
        else:
            dp[i] = dp[i-1] + 1
            prev[i] = i-1



    print(dp[n])  
    ret_arr = []
    i = n
    while prev[i] != 0:
        ret_arr.append(prev[i])
        #print(prev[i], end=' ')
        i = prev[i]
    for i in ret_arr[-1::-1]:
        print(i, end=' ')
    
    print(n)
