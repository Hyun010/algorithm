n=int(input())
num=[]
for _ in range(n):
    a,b=map(int,input().split())
    num.append(a+b)
print(*num,sep='\n')