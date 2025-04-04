""" 
Write a program to take a number from the user and output whether that number is negative, positive or zero.

Test Case1:
Input:
6
Output:
Positive

Test Case2:
Input:
0
Output:
Zero
 """
 
 
num=int(input("enter "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")