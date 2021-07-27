""" # Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
# Sample Inputs:
# hello -> True
# nono -> False
# sunday -> False
# racecar -> False
 """

def double_letters(string):
    l=[]
    for i in string:
        l.append(i)
    count = 0
    while count < len(l) - 1:
        if l[count] == l[count+1]:
            return True    
        count = count+1
    return False 

print(double_letters("hello"))