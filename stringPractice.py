# name = "mark"

# print(name.upper())
# print(name.capitalize())
# print(name[::-1])

# string = input('Please enter a word: ').upper()

# string = string.replace('A', '4')
# string = string.replace('E', '3')
# string = string.replace('G', '6')
# string = string.replace('I', '1')
# string = string.replace('O', '0')
# string = string.replace('S', '5')
# string = string.replace('T', '7')

secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
offset = 13
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''

for char in secret:
    ascii_code = ord(char)
    is_uppercase = ascii_code >= 65 and ascii_code <= 90
    char = char.lower()
    if char not in alphabet:
        new_char = char
    else:
        idx = alphabet.find(char)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
        new_char = alphabet[new_idx]
        if is_uppercase:
            new_char = new_char.upper()
    result += new_char

print(result)