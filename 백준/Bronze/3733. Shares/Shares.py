while True:
    try:
        N,S=map(int,input().split())
    except:
        break
    else:
        print(S//(N+1))