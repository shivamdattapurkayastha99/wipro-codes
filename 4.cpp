// the it giant .........
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int n;
    cin>>n;
    int arr[10];
    arr[0]=1;
    arr[1]=1;
    arr[2]=1;
    arr[3]=1;
    arr[4]=0;
    arr[5]=1;
    arr[6]=0;
    arr[7]=1;
    arr[8]=0;
    arr[9]=0;
    int sum=0;
    while (n>0)
    {
        int r=n%10;
        if (arr[r]==0)
        {
            sum+=r;

        }
        n/=10;
    }
    cout<<sum;
    


    return 0;
}
