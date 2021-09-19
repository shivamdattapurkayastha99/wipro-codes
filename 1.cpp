// a company provides data encryption to ...........
#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    int k;
    string s;
    cin>>k>>s;
    string ans="";
    for (int i = 0; i <s.length(); i++)
    {
        char x=s[i];
        x+=k;
        ans+=x;

    }
    cout<<ans;
    
    return 0;
}
