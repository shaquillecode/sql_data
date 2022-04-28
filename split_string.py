"""Write a function that takes a string of chars, digits and symbols and returns a count of each one."""
import os
from statistics import mode

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes


# i.e.
# str1 = "P@#yn26at^&i5ve" -> Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4

str1 = "P@#yn26at^&i5ve"

def splitString(str1):
    '''Splits The String into Chars, Digits, & Symbols'''
    alpha = ""
    num = ""
    symbols = ""
    for i in range(len(str1)):
        if (str1[i].isdigit()):
            num = num + str1[i]
        elif((str1[i] >= 'A' and str1[i] <= 'Z') or (str1[i] >= 'a' and str1[i] <= 'z')):
            alpha += str1[i]
        else:
            symbols += str1[i]

    print(alpha)
    print(num )
    print(symbols)
    print(f"This is the count for chars {len(alpha)}")
    print(f"This is the count for digits {len(num)}" )
    print(f"This is the count for symbols {len(symbols)}")



splitString(str1)


# Part 1 Find Most common Letter in text
text = "Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs. These might be considered part of the programming process, but often the term software development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code. Software engineering combines engineering techniques with software development practices. Reverse engineering is a related process used by designers, analysts and programmers to understand and re-create/re-implement"

print("The original text is : " + str(text))
# getting all letters of each word in text
listcom1 = [wrd for sub in text for wrd in sub.split()]
# Finding most frequent letter
freq_letter = mode(listcom1)
print("Letter with maximum frequency : " + str(freq_letter))


# Part 2 Find Most common word in text list
text_list = []
for i in text.split():
    text_list.append(i)

# getting word frequency
freq_word = mode(text_list)

print("Word with maximum frequency : " + str(freq_word))
