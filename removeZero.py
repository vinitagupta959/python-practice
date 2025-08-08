"""Problem Statement:
Write a program that takes an array of integers as input using the map() function, and then removes all zero elements from the array using a while loop. After removing the zeroes, print the resulting array with elements separated by spaces.


Constraints:
Use the map() function to take the input in a single line.
Use only a while loop for repetition.
Do not use any inbuilt functions or methods for removing zeroes.
The array will contain at least one element.



Sample Input 1:
1 0 3 0 5 0

Sample Output 1:
1 3 5



Sample Input 2:
7 0 9 0 10

Sample Output 2:
7 9 10

"""

arr=list(map(int, input().split()))
i=0
k=0
while i<len(arr):
  if arr[i]!=0:
    arr[k]=arr[i]
    k+=1
  i+=1
arr=arr[:k] #array ki len ko resize kar rhe to baki array ke item delete ho jayenge 
i=0
while i<len(arr):
  print(arr[i],end=" ")
  i+=1