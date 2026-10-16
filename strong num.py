
a=int(input("give:"))
b=a 
v=0
while a>0:
    e=a%10
    f=1
    for m in range (1,e+1):
        f=f*m
    v=v+f
    a=a//10
if b == v:
    print(f"{b} is a strong number")
else:
    print(f"{b} is not a strong number")