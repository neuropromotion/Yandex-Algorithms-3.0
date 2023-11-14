/*
9. Сумма в прямоугольнике
Ограничение времени	3 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с левым верхним углом (x1, y1) и правым нижним (x2, y2)

Формат ввода
В первой строке находится числа N, M размеры матрицы (1 ≤ N, M ≤ 1000) и K — количество запросов (1 ≤ K ≤ 100000). Каждая из следующих N строк содержит по M чисел`— элементы соответствующей строки матрицы (по модулю не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных пробелом x1 y1 x2 y2 — запрос на сумму элементов матрице в прямоугольнике (1 ≤ x1 ≤ x2 ≤ N, 1 ≤ y1 ≤ y2 ≤ M)

Формат вывода
Для каждого запроса на отдельной строке выведите его результат — сумму всех чисел в элементов матрице в прямоугольнике (x1, y1), (x2, y2)
*/
#include <iostream>
#include <vector>
#include <algorithm> 
#include <sstream>
typedef long long ll;
using namespace std;

int main()
{
    ll n, m, q;
    cin >> n >> m >> q;  
    vector <vector<ll>> matrix(n, vector<ll>(m)); 
    string str;
    int ans[q];
    int j = 0; 
    for (int i = -1; i < n; i++) 
    { 
        getline(cin, str);  
        istringstream ss(str); 
        while(ss >> matrix[i][j++] && j < m);
        j = 0;
    }  
    vector<vector<ll>> prefix (n, vector<ll>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j ++)
        {  
            prefix[i][j] = matrix[i][j];
            if (i)
                prefix[i][j] += prefix[i - 1][j]; 
            if (j)
                prefix[i][j] += prefix[i][j - 1];
            if (i && j)
                prefix[i][j] -= prefix[i - 1][j - 1];
        } 
     for(int i = 0; i < q; i++)
    {
        ll x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;
        x1--;
        y1--;
        x2--;
        y2--;
        int sum = prefix[x2][y2];
        if (x1)
            sum -= prefix[x1-1][y2];
        if (y1)
            sum -= prefix[x2][y1 - 1];
        if (x1 && y1)
            sum += prefix[x1 - 1][y1 - 1]; 
        ans[i] = sum;
    }
    for(int i = 0; i < q; i++)
        cout << ans[i] << endl;
    return 0;
} 
