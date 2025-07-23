# Write a Python program to find the frequency of each element in a list without using for loops, methods (like append(), count()), or dictionaries. Use only while loops and basic list operations.
arr = [1, 2, 2, 3, 1, 4, 2]
n = len(arr)
i = 0
visited = []

while i < n:
    current = arr[i]
    already_counted = False
    j = 0
    while j < len(visited):
        if visited[j] == current:
            already_counted = True
            break
        j += 1

    if not already_counted:
        freq = 0
        k = 0
        while k < n:
            if arr[k] == current:
                freq += 1
            k += 1

        print(current, "→", freq, "times")
        visited=visited+[current]  

    i += 1


# Second way
# In this method, we are not using any extra array to store visited elements.This code is faster and has better time efficiency. But, unlike the first way, we cannot reuse the original array after running this,because we are modifying it by marking counted elements as -1.
arr1 = [1, 2, 2, 3, 1, 4, 3]
n = len(arr)
i = 0
while i < n:
    if arr1[i] != -1:
        current = arr1[i]
        freq = 0
        j = 0
        while j < n:
            if arr1[j] == current:
                freq += 1
                arr1[j] = -1
            j += 1
        print(current, "→", freq, "times")
    i += 1
