""" Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0] """
nums=list(map(int,input().split()))
i = 0   
j = 0  

while j < len(nums):
    if nums[j] != 0: 
        print(i)
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i += 1 
    j += 1  
    print(nums) 