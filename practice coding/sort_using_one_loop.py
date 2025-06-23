arr = [5, 2, 9, 1, 3]
i = 0
 
while i < len(arr) - 1:
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = 0
    else:
        i += 1
 
print(arr)