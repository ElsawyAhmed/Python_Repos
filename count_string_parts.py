'''
    this script accepts a string and calculate the number of digits, letters and special characters.
'''
string = input("Please Enter a string containig numbers and special characters : \n")

digits=letters=special=0

for character in string:
    if character.isdigit():
        digits=digits+1
    elif character.isalpha():
        letters=letters+1
    else:
        special=special+1

print("Letters Count : ", letters)
print("Digits Count  : ", digits)
print("Special Characters  Count  : ", special)