# hacker and bank problem 
# a bank account requires a security passkey....
def ans(s):
    l=list(map(str,s.strip()))
    ans=[]
    vowel=['a', 'e', 'i', 'o', 'u']
    for i in range(len(l)):
        if str(l[i]) in vowel:
            l[i].replace(l[i],"")
    for i in range(len(l)):
        if len(l[i])>0 and str(l[i]) not in vowel:
            ans.append("*")
            ans.append(str(l[i]))
        else:
            ans.append(str(l[i]))
    for i in range(len(ans)):
        if ans[i]>='A' or ans[i]<='Z':
            ans[i]=ans[i].lower()        
    print("".join(ans))

for _ in range(int(input())):
    s=input()
    ans(s)

