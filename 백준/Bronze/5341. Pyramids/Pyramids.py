def pyramid(x):
    cnt=0
    if x==1:
        return cnt+1
    else:
        return cnt+x+pyramid(x-1)

num_list=[]
while True:
    base=int(input())
    if base==0:
        break
    num_list.append(pyramid(base))

for num in num_list:
    print(num)