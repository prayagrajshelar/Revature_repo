def common_prefix(strings):

    prefix = strings[0]
    for i in strings[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

print(common_prefix(["flower","flow","flight","flamingo","fly"]))
print(common_prefix(["dog","racecar","car"]))



# Write a function to find the longest common prefix string amongst an array of strings.
 
# If there is no common prefix, return an empty string "".
 
# Example 1:
 
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
 
# All given inputs are in lowercase letters a-z.

