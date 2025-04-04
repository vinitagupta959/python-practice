""" Write a program to take four numbers from the user and print the greater number of the four numbers. (assume all the numbers are distinct).

Test Case1:
Input:
98
13
29
58
Output:
98
 """
 
a=int(input())
b=int(input())
c=int(input())
d=int(input())
max=0
max1=0
if a>b:
    max=a 
else:
    max=b 
if c>d:
    max1=c 
else:
    max1=d 
if max>max1:
    print(max)
else:
    print(max1)
    