# power of 2
# I/P=7
#O/P=nO
#I/P=256
#O/P=yes

num=int(input())
result="No"
multi=0
if num>0:
    if num%2==0:
        multi=num%2
        if multi%2==0:
            result="Yes"
print(result)
    
    
    