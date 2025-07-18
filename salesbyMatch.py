# Given an array of intergers representing the colio of each sock, determine how many pair of socks with matching colos there. For example , there are 7 socks with colors[1,2,1,2,1,3,2]. there is one pair of color 1 and one of color 2. There are three odd socks left one of each color. The number of pairs is 2.

# Create a function that returns an integer repesenting the number of matching pairs of spcks that are available.
# example:- sockMerchant([10,20,20,10,30,50,10,20])
# output is 3

arr=list(map(int, input().split()))
arr2=sorted(arr)
count=0
pair=0
i=0
j=1
print(arr2)
while i < len(arr2):
    if arr2[i] == arr2[i+1]:
        pair += 1
        i += 2 
    else:
        i += 1  
print(pair)
