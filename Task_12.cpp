/*
12. Правильная скобочная последовательность
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа должна определить, является ли данная скобочная последовательность правильной. Пустая последовательность является правильной. Если A — правильная, то последовательности (A), [A], {A} — правильные. Если A и B — правильные последовательности, то последовательность AB — правильная.

Формат ввода
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Формат вывода
Если данная последовательность правильная, то программа должна вывести строку "yes", иначе строку "no".
*/

#include <iostream>
#include <vector> 
using namespace std;

class Stack
{
    private:
        vector<char>seq;
    public:
        Stack (string st)
        {
            this->seq.reserve(st.size());
            for (int i = 0; i < st.size(); i ++)
            {
                this->seq[i] = st[i];
            }
        }
        bool exam(char x)
        {
            if ((x == '(') || (x == '{') || (x == '['))
            {
                this->seq.push_back(x); 
                return true;
            }
            else
            {
                if (this->seq.size())
                {
                    if ((x == ']') && (this->seq.back() == '['))
                    {
                        this->seq.pop_back();
                        return true;
                    }
                    if ((x == '}') && (this->seq.back() == '{'))
                    {
                        this->seq.pop_back();
                        return true;
                    }
                    if ((x == ')') && (this->seq.back() == '('))
                    {
                        this->seq.pop_back();
                        return true;
                    }
                }
                return false;
            }
        }
        void ans()
        {
            if (this->seq.size())
                cout << "no" << endl;
            else
                cout << "yes" << endl;
        }     
};

int main()
{
    string st; 
    getline(cin, st);
    if (st.size() == 0)
    {
        cout << "yes" << endl;
        return 0;
    }
    Stack * stack = new Stack(st);
    vector <char> seq(st.size());
    for (int i = 0; i < st.size(); i++)
    { 
        seq[i] = st[i]; 
    }

    bool ind = true;
    while (seq.size() && (ind))
    {
        ind = stack->exam(seq[0]);
        seq.erase(seq.begin());
    }   
    if (ind)
        stack->ans();
    else
        cout << "no" << endl; 
}
