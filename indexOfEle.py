"""Problem Statement:
Write a program that takes an array of integers and an integer x as input. The program should find and print the index of the first occurrence of x in the array using a while loop. If x is not found in the array, print -1.


Constraints:
Use the map() function to take the input in a single line.
Use only a while loop for repetition.
Do not use any inbuilt functions or methods for finding the index.
The array will contain at least one element.



Sample Input 1:
1 2 3 4 5
3
Sample Output 1:
2
(Explanation: The first occurrence of 3 is at index 2.)



Sample Input 2:
7 8 9 10
5
Sample Output 2:
-1
(Explanation: 5 is not found in the array.)

"""

arr=list(map(int, input().split()))
target=int(input())
i=0
found="No"
while i<len(arr):
  if arr[i]==target:
    print(i)
    found="Yes"
    break
  i+=1
if found=="No":
  print(-1)