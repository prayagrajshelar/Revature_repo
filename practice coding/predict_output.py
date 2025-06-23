def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))



funcs = [lambda x: x+i for i in range(3)]
results = [f(10) for f in funcs]
print(results)


a = [1,3,4]
b = [1,3,4]
print(a is b)
print(a == b)


a=[1,0,5,0,6,2,0,9]
b = []
for i in a:
    if i == 0:
        b += [i]
        a.remove(i)
c = sorted(a)+b
print(c)





nums = [1, 2, 3, 4,3,2,5,4,2,2,65,6,43,43,1,23,453,23,3,32,2,4,2,4,6,4,2,443,2,1,2,3,4,3,2,3]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)
print(nums)


print("abc"*0)