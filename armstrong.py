a=int(input())
#b=len(str(a))
temp=a
su=0
while temp>0:
    d=temp%10
    temp=temp//10
    su=su+d*d*d
    
if(su==a):
    print("armstrong num")
else:
    print("not")


