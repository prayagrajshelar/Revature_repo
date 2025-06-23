num = int(input("Enter a decimal number: "))
print(bin(num)[2:])

# Same logic for finding --------- Octal => oct() -------- Hexadecimal => hex() ---------- numbers

# OR

binary = ""
if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

print(binary)
