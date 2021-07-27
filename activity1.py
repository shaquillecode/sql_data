"""
ASCII (American Standard Code for Information Interchange), is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.

There is a function for finding the ascii value of a character here: https://docs.python.org/3/library/functions.html

Write a function that asks the user for input, and then computes the sum of all the ascii values of the characters.

"hello" -> 104 + 101 + 108 + 108 + 111 = 532
Part 2: Given a list of words (from user input) determine which word has the highest ascii value.
"""
def Mysum2(string):
    total = 0
    for ch in string:
        ascii_val = ord(ch)
        total += ascii_val
        print((f"character {ch} / value {ascii_val}"))
    return total
string = "My name is SHAQ"
string2 = "My name is Dom"
total = Mysum2(string)
print((f"this is the total {total}"))


# or


def input_word():

	while True:
		try:
			wd = input('Enter a word:\n').strip()
			break
		except ValueError:
			print("Enter a string!!, wrong value type")	
	return wd

def ascii_calculator(n=1):

	all_words = []
	while n:
		wd = input_word()	
		n -= 1
		val = (wd, sum(ord(char) for char in wd))
		print((f"the ascii value of {val[0]} is { val[1]}"))
		all_words.append(val)
	return all_words 
if __name__ == '__main__':
	ascii_val = ascii_calculator()
	print(ascii_val)

	ascii_val = ascii_calculator(2)
	print(ascii_val)
