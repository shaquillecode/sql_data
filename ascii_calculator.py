"""
ASCII (American Standard Code for Information Interchange),
is a character encoding standard for electronic communication.
ASCII codes represent text in computers, telecommunications equipment, and other devices.

Function for ascii value of a character here: https://docs.python.org/3/library/functions.html

Write a function that asks the user for input,
And computes the sum of all the ascii values of the characters.

"hello" -> 104 + 101 + 108 + 108 + 111 = 532
"""
def input_word():
    '''input_word'''

    while True:
        try:
            WD = input('Enter a word:\n').strip()
            break
        except ValueError:
            print("Enter a string!!, wrong value type")
    return WD

def ascii_calculator(num=1):
    '''ascii_calculator'''

    all_words = []
    while num:
        WD = input_word()
        num -= 1
        val = (WD, sum(ord(char) for char in WD))
        print((f"the ascii value of {val[0]} is { val[1]}"))
        all_words.append(val)
    return all_words
if __name__ == '__main__':
    ascii_calculator()
