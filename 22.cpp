#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int n,i,j,c=1;
    cin>>n;
    for (i = 1; i <=n; i++)
    {
        for (j = 1; j <=i; j++)
        {
            if (j<i)
            {
                cout<<to_string(c)+ "*";
                c++;

            }
            else
            {
                cout<<to_string(c);
                c++;
            }
            
        }
        cout<<"\n";

        
    }
    c=c-n;
    for ( i = n; i >=1; i--)
    {
        for ( j = 1; j <=i; j++)
        {
           if (j<i)
           {
               cout<<to_string(c) +"*";
               c++;
           }
           else
            {
                cout<<to_string(c);
                c++;
            }
           
        }
        c=(c+1)-2*i;
        cout<<'\n';
        
    }
    
    return 0;
}
