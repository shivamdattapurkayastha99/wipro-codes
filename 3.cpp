// the online math course provider..
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int n,digit;
    cin>>digit>>n;
    int count=0;
    while (n>0)
    {
        int r=n%10;
        if (r!=digit)
        {
            count++;
        }
        n/=10;
    }
    cout<<count;
    
    return 0;
}

