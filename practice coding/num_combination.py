a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

nums = [a,b,c]

print("All Combinations are: ")

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i != j and j != k and i != k:
                print(nums[i], nums[j], nums[k])


