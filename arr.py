# firstly we incilise i for indexing.
# we use while loop and under the loop we check if arr[i]equl to value.
# if yes so print the indexing and beack the loop.

arr=[4,1,7,3,9,2,8,5,0,6];
value=20
i=0
while i<len(arr):
    if arr[i]==value:
        print("index",i)
        break
    i+=1
if len(arr)==i:
    print("Not find")
