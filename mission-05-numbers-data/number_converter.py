# number converter - takes a decimal number and shows binary and hex

num = int(input("Enter a positive decimal number: "))

binary = bin(num)
hexa = hex(num)

print("Binary:", binary)
print("Hexadecimal:", hexa)

# bin() and hex() add 0b / 0x in front, so showing without it too
print("Binary (no prefix):", binary[2:])
print("Hex (no prefix):", hexa[2:].upper())
