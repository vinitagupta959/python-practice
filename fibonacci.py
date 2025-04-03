target=2578
a=0
b=1
c=0
i=1
while i<target:
    c=a+b
    a=b
    b=c
    i+=1
print(c)