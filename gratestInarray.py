
""" Find Greatest Common Divisor of Array
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2. """



def findGCD():
    nums=list(map(int, input().split()))
    i=0
    min=nums[i]
    max=nums[i] 
    while i<len(nums):
        if nums[i]<=min:
            min=nums[i] 
        if nums[i]>=max:
            max=nums[i]
        i+=1
    i=1
    hcf=1
    while i<=min:
        if min%i==0:
            if max%i==0:
                hcf=i
        i+=1
    return hcf
print(findGCD())


