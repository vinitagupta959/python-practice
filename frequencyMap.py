nums = list(map(int, input().split()))
freqMap = {}

i = 0
while i < len(nums):
    num = nums[i]
    if num in freqMap:
        freqMap[num] += 1
    else:
        freqMap[num] = 1
        # as we know if any kry is not present in object do it make 
    i += 1
keys = list(freqMap.keys())
j = 0
while j < len(keys):
    key = keys[j]
    print(key, "→", freqMap[key], "times")
    j += 1



# second why
arr=list(map(int, input().split()))
hash_map={}
n=len(arr)
for i in range (0,n):
    hash_map[arr[i]]=hash_map.get(arr[i],0)+1
"""
.get(key, default_value)
→ Ye method check karta hai:
Agar key present hai dictionary mein → uski value return karta hai.
Agar key nahi hai → jo default value diya hai, wo return karta hai.
"""

for key in hash_map:
    print(key, "→", hash_map[key], "times")
