"""
 Define a function named double_letters that takes a single parameter. The parameter is a string.
 Your function must return True if there are two identical letters in a row in the string, and False otherwise.
 Sample Inputs:
 hello -> True
 nono -> False
 sunday -> False
 racecar -> False
 """

def double_letters(string):
    '''Prints if string has consecutive Double Letter'''
    the_list=[]
    for i in string:
        the_list.append(i)
    count = 0
    while count < len(the_list) - 1:
        if the_list[count] == the_list[count+1]:
            return True
        count = count+1
    return False

print(double_letters("hello"))
