num = int(input("Enter a number: "))

multiple = 1
addition = 0

while num > 0:
    rem = num % 10
    multiple *= rem
    addition += rem
    num = num // 10

print(multiple-addition)


# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15
# Example 2:
 
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21