import array as ar

array1 = ar.array('i',[1,2,3,4])
array2 = ar.array('i',[5,6,7,8])

merged_array = array1 + array2
print(merged_array)
print(list(merged_array))