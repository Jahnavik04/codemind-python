n=int(input())
a=list(map(int,input().split()))
r=int(input())
r%=n
for i in range(r):
    c=a.pop()
    a.insert(0,c)
print(*a)