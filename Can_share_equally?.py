a,b=map(int,input().split())
if a%2!=0 or  (b%2!=0 and a==0) :
    print("NO")
else:
    print("YES")