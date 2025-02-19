while True:
    try:
        a,b=map(int,input().split())
    except:
        break
    else:
        if a==0 and b==0:
            break
        elif a<=b:
            print("No")
        else:
            print("Yes")