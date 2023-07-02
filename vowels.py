#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      singh
#
# Created:     02-07-2023
# Copyright:   (c) singh 2023
# Licence:     <your licence>
#--------------------------------------------------------------------------


def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)


input_string = input("Enter a string: ")
result = remove_vowels(input_string)
print("Result:", result)
