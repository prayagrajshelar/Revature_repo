# Password Validator

import re
def valid_pass(password):
    pattern = r"""
        ^                   
        (?=.*[a-z])       
        (?=.*[A-Z])         
        (?=.*\d)            
        (?=.*[@#$%^&+=!])   
        [A-Za-z\d@#$%^&+=!]{8,}  
        $                  
        """
    return bool(re.match( pattern, password, re.VERBOSE))

password = input("Enter your password: ")
if valid_pass(password):
    print("Valid Password")
else:
    print("Invalid Password, Try again!")



# URL Validator

import re
def valid_url(url):
    pattern = r"""
    ^
    (https?://)?
    (www\.)?
    (localhost|[a-zA-Z0-9-]+\.[a-zA-Z]{2,})
    (:\d+)?
    (/?|/\S*)?
    $
    """
    return (re.match(pattern, url, re.VERBOSE))

url = input("Enter your url: ")
if valid_url(url):
    print("Valid url")
else:
    print("Invalid url, Try again !")


# Exception Handling

# ZeroDivisionError
try:
    num = 10/0
except ZeroDivisionError as e:
    print("Zer Division Error:",e)

try:
    num = int("Abs")
except ValueError as e:
    print("Value Error: ",e)

try:
    a = '5' + 10
except TypeError as e:
    print("Type Error: ",e)

try:
    lst = [1,2,3]
    print(lst[10])
except IndexError as e:
    print("Index Value Error: ",e)


try:
    dictionary = {"name":"Prayagraj"}
    print(dictionary["age"])
except KeyError as e:
    print("Key error: ",e)

try:
    name = "Prayagraj"
    name.push("Hello")
except AttributeError as e:
    print("Attribute Error: ",e)

try:
    f = open("notexisted.txt","r")
except FileNotFoundError as e:
    print("File Not Found Error: ", e)

try:
    import module
except ModuleNotFoundError as e:
    print("Module Not found error: ", e)

try:
    print(q)
except NameError as e:
    print("Name Error: ",e)