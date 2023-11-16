/*
17. Игра в пьяницу
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот, чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без карт – проигрывает. Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает самую старшую карту ("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды). Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует 10 карт, имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.

Формат ввода
Программа получает на вход две строки: первая строка содержит 5 чисел, разделенных пробелами — номера карт первого игрока, вторая – аналогично 5 карт второго игрока. Карты перечислены сверху вниз, то есть каждая строка начинается с той карты, которая будет открыта первой.

Формат вывода
Программа должна определить, кто выигрывает при данной раздаче, и вывести слово first или second, после чего вывести количество ходов, сделанных до выигрыша. Если на протяжении 106 ходов игра не заканчивается, программа должна вывести слово botva.
*/
#include <iostream>
#include <vector>
using namespace std;

class Queue
{
    private:
    vector <int> cards;
    public:
    Queue (int * vals)
    {   
        for(int i = 0; i < 5; i++)
            this->cards.push_back(vals[i]); 
    }
    void push (int val1, int val2)
    {
        this->cards.push_back(val1);
        this->cards.push_back(val2);
    }
    int pop ()
    {
        int temp = this->cards.front();
        this->cards.erase(this->cards.begin());
        return temp;
    }
    int front ()
    {
        return this->cards.front();
    }
    int size()
    {
        return this->cards.size();
    }
    void print()
    {
        for (int i = 0; i < this->cards.size(); i++)
        {
            cout << cards[i] << ' ';
        }
        cout << endl;
    }
};



int main()
{
    int arr_1[5];
    int arr_2[5];
    for (int i = 0; i < 5; i++)
        cin >> arr_1[i]; 
    for (int i = 0; i < 5; i++)
        cin >> arr_2[i];     

    Queue * player_one = new Queue(arr_1);
    Queue * player_two = new Queue(arr_2);  
    int counter_of_rounds = 0;
    while ((counter_of_rounds != 1000000) && (player_one->size()) && (player_two->size()))
    {
        if (player_one->front() > player_two->front())
        {
            if(player_one->front() == 9 && player_two->front() == 0)
            {
                player_two->push(player_one->pop(), player_two->pop());
                counter_of_rounds++;
                continue;
            }
            player_one->push(player_one->pop(), player_two->pop());
            counter_of_rounds++;
            continue;
        }
        else
        {
            if(player_two->front() == 9 && player_one->front() == 0)
            {
                player_one->push(player_one->pop(), player_two->pop());
                counter_of_rounds++;
                continue;
            }
            player_two->push(player_one->pop(), player_two->pop());
            counter_of_rounds++;
            continue;
        }
    }

    if (!(player_one->size()))
    {
        cout << "second " << counter_of_rounds << endl;
        return 0;
    }
    else if (!(player_two->size()))
    {
        cout << "first " << counter_of_rounds << endl;
        return 0;
    }
    cout << "batva" << endl;
    return 0;
}