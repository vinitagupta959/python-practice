""" Write a program to take a number from the user and check whether the last digit of a number (entered by the user) is divisible by 3 or not.

	Test Case1:
	Input:
	453
	Output:
	YES

	Test Case2:
	Input:
	435
	Output:
	No """
 
 
num=int(input())
num=num%10
if num%3==0:
    print("Yes")
else:
    print("No")