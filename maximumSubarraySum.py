# Maximum sumarray Sum
n=int(input())
arr=list(map(int, input().split()))
start=0
maxNum=arr[0]
bestSub=[]
while start<n:
    end=start
    sumNum=0
    curentSub=[]
    while end<n:
        sumNum+=arr[end]
        curentSub+=[arr[end]]
        end+=1
    if sumNum>maxNum:
        maxNum=sumNum
        bestSub=curentSub
    start+=1
print(maxNum)
print(bestSub)




""" Given an integer array nums, find the subarray with the largest sum, and return its sum.
 
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23. """

# isme edge case nhi chutenge or currect max ayega upr vale me currect nhi aa rha 


n=int(input())
arr=list(map(int,input().split()))
currentSum=0
maxSum=0
i=0
while i<n:
    curentSub+=arr[i]
    if maxSum<currentSum:
        maxSum=currentSum
        # ye condition hamne badme isliye dala hai ki is hamare pass sare nagativ number ho to usme atleast ek max to ayega 
    if currentSum<0:
        currentSum=0
    i+=1
