"""Problem Statement:
Write a program that takes an array of integers as input using the map() function, and then removes all negative numbers from the array using a while loop. Print the modified array, with the remaining elements separated by spaces.





Constraints:
Use the map() function to take the input in a single line.
Use only a while loop for repetition.
Do not use any inbuilt functions or methods for removing the negative numbers.
The array will contain at least one element.



Sample Input 1:
1 -2 3 -4 5
Sample Output 1:
1 3 5



Sample Input 2:
-7 -8 9 10
Sample Output 2:
9 10

"""


arr=list(map(int, input().split()))
i=0
while i<len(arr):
  if arr[i]<0:
    arr.pop(i)
  else:
    i+=1 
i=0
while i<len(arr):
  print(arr[i],end=" ")
  i+=1