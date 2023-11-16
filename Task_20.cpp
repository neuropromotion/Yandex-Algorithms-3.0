/*
20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.
*/
#include <stdio.h>
#include <iostream>
void shiftDown (int * numbers, int root, int bottom);
void heapSort (int * numbers, int array_size);
int main (void)
{  
	using namespace std;
    int n;
	cin >> n;
	int arr[n];
	for (int i = 0; i < n; i++)
    	cin >> arr[i];
	heapSort(arr, n);
	for (int i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout<<endl;
	return 0;
} 


void shiftDown (int * numbers, int root, int bottom)
{
    int maxChild; 
    bool done = false; 
    while ((root * 2 <= bottom) && (!done)) 
    {
        if (root * 2 == bottom)
        {
            maxChild = root * 2;
        } else if (numbers[root * 2] > numbers [root * 2 + 1])
        {
            maxChild = root * 2;
        } else maxChild = root * 2 + 1;
        if (numbers[root] < numbers[maxChild]) 
        {
            int tmp;
            tmp = numbers[root];
            numbers[root] = numbers[maxChild];
            numbers[maxChild] = tmp;
            root = maxChild;
        }
        else done = true; 
    }

}
void heapSort (int * numbers, int array_size)
{
    for (int i = array_size / 2; i >= 0; i--) 
        shiftDown(numbers, i, array_size - 1); 
    for (int i = array_size - 1; i >= 1; i--)
    {
        int tmp = numbers[0];
        numbers[0] = numbers[i];
        numbers[i] = tmp;
        shiftDown(numbers, 0, i - 1);
    }
}
