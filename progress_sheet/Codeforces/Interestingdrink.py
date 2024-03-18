import bisect
n=int(input())
lst=list(map(int,input().split()))
q=int(input())
res=[]
for i in range(q):
    res.append(int(input()))
lst.sort()
for num in res:
    print(bisect.bisect_right(lst,num))