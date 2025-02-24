cnt=0
total=0
while cnt<5:
    a=int(input())
    if a<0 or a>100:
        break
    total+=a
    cnt+=1
print(total)