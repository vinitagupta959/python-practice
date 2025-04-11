""" 
Write a program to take 4 numbers from the user and output the second max of 4 numbers.

Test Case1:
Input:
5
4
6
7
Output:
6
 """
 
 


a=int(input())
b=int(input())
c=int(input())
d=int(input())
maxSec=0
secMax=0
if a>b:
    maxSec=a
    secMax=b 
else:
    maxSec=b 
    secMax=a 
if(c>d):
    if c>maxSec:
        secMax=maxSec 
    else:
        if c>secMax:
            secMax=c
else:
    if d>maxSec:
        secMax=maxSec
    else:
        if d>secMax:
            secMax=d
print(secMax)
        