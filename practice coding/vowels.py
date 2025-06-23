input_str = input("Enter a string: ")



# vowels = ['a','e','i','o','u']
# count = 0
# str_vowels = ''
# for i in input_str:
#     if i in vowels:
#         count+=1
#         str_vowels+=i
# print(count)
# print(str_vowels)


def info(input_str):
    capital_count = 0
    lower_count = 0
    num_count = 0

    for i in input_str:
        if i>0 and i<9:
            num_count+=1
        elif i.isupper():
            capital_count+=1
        elif i.islower():
            lower_count+=1
    return num_count, capital_count, lower_count

print(info(input_str))