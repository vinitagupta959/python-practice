# minimum and maximum subarray sum
n=int(input())
arr=list(map(int, input().split()))
start=0
maxNum=arr[0]
minNum=arr[0]

while start<n:
    end=start
    while end<n:
        i=start
        sumNum=0
        while i<=end:
            sumNum+=arr[i]
            i+=1
        end+=1
        if sumNum>maxNum:
            maxNum=sumNum
        if minNum>sumNum:
            minNum=sumNum
    start+=1
print(maxNum,minNum)
