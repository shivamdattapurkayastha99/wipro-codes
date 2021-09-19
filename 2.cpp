// the games developer gamingFun...
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    string s;
    getline(cin,s);
    int i=s.length()-1;
    int count=0;
    while (i>=0 and s[i]==' ')
    {
        i--;

    }
    while (i>=0 and s[i]!=' ')
    {
        count++;

        i--;
        
    }
    cout<<count;
    return 0;
}
