# using two poniter reverse array.
arr=[1,2,4,5]
start=0
end=len(arr)-1
tem=0
while start<end:
    temp=arr[start]
    arr[start]=arr[end]
    arr[end]=temp 
    start+=1
    end-=1
print(arr)