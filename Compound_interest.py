p,r,t=map(int,input().split())
CI=p*(pow((1+r/100),t))
print('{:.2f}'.format(CI))