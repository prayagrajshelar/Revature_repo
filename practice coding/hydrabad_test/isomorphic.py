s1 = input()
s2 = input()

temp1 = list(set(s1))
temp2 = list(set(s2))

if len(temp1) == len(temp2):
    print("True")
else:
    print("False")