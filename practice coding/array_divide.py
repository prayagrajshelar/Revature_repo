nums = [1,2,3,4]
k = 3
if len(nums) % k == 0:
    print("True")
else:
    print("False")


# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# Example 2:
 
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
# Example 3:
 
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# Example 4:
 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.

# ----------------------------------------------------------------------------------------------------

from collections import Counter

def canDivideIntoSets(nums, k):
    if len(nums) % k != 0:
        return False

    count = Counter(nums)
    nums_sorted = sorted(count)
    result = []

    for num in nums_sorted:
        while count[num] > 0:
            group = []
            for i in range(k):
                if count[num + i] == 0:
                    return False
                count[num + i] -= 1
                group.append(num + i)
            result.append(group)

    print("Partitions:", result)
    return True

# Test cases
print(canDivideIntoSets([1,2,3,3,4,4,5,6], 4))         # True
print(canDivideIntoSets([3,2,1,2,3,4,3,4,5,9,10,11], 3)) # True
print(canDivideIntoSets([3,3,2,2,1,1], 3))              # True
print(canDivideIntoSets([1,2,3,4], 3))                  # False



# ---------------------------------------------------------------------------------------------------------




def canDivideIntoSets(nums, k):
    if len(nums) % k != 0:
        return False

    # Build frequency dictionary manually
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []
    sorted_nums = sorted(freq.keys())

    for num in sorted_nums:
        while freq.get(num, 0) > 0:
            group = []
            for i in range(k):
                current = num + i
                if freq.get(current, 0) == 0:
                    return False
                freq[current] -= 1
                group.append(current)
            result.append(group)

    print("Partitions:", result)
    return True

# Test cases
print(canDivideIntoSets([1,2,3,3,4,4,5,6], 4))         # True
print(canDivideIntoSets([3,2,1,2,3,4,3,4,5,9,10,11], 3)) # True
print(canDivideIntoSets([3,3,2,2,1,1], 3))              # True
print(canDivideIntoSets([1,2,3,4], 3))                  # False

