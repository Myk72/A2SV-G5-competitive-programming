from collections import Counter
for i in range(int(input())):
    n=int(input())
    string=input()
    prev=0
    count=Counter({0:1})
    res=0
    for idx,num in enumerate(string):
        prev+=int(num)-1
        res+=count[prev]
        count[prev]+=1
        #print(res,idx,prev)
    print(res)