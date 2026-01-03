#Count Elements Less Than the Average of First and Last Element in an Array

n=int(input())
arr=list(map(int, input().split()))
count=0
i=0
avg=(arr[0]+arr[n-1])/2
while i<n:
    if arr[i]<avg:
        count+=1
    i+=1
print(count)
