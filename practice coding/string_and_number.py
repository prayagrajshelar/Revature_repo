# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
# If the following string is given as input to the program:


# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
 
# Then, the output of the program should be:


# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ



def wrap_string(string, width):
    for i in range(0, len(string), width):
        print(string[i:i+width])
wrap_string("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)