a=int(input())
t=0
for i in range(1,a):
    if a%i ==0:
        t+=i
if t==a:
    print("True")
else:
    print("False")