n=int(input())
list=[]
for _ in range(n):
    word=input()
    list.append(word[0]+word[-1])
print(*list,sep='\n')