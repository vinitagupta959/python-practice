""" 
Write a program to take a number from the user and check whether a number is a 4-digit number and it should be divisible by 7 and its quotient after dividing by 7 should be even.

Test Case1: 
	Input: 
	9999
	Output:
	No
	
	Test Case2:
	Input: 
	9821
	Output: 
	No

	Test Case3:
	Input: 
	3514
	Output:
	Yes 
 """
 
num=int(input())
ques=0
if num>999 and num<10000:
    if num%7==0:
        ques=num//7
        print(ques)
        if ques%2==0:
            print("Yes")
    else:
        print("No")
else:
    print("No")