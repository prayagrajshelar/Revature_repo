# Please write a program which accepts a string from console and print the characters that have even indexes.
# Example: If the following string is given as input to the program:
# Plain Text
# H1e2l3l4o5w6o7r8l9d
 
# Then, the output of the program should be:
# Plain Text
# Helloworld


string1 = "H1e2l3l4o5w6o7r8l9d"
list = [1,2,3,4,5,6,7,8,9]
str = ""
for i in string1:
    if i.isdigit():
        continue
    else:
        str+=i
print(str)