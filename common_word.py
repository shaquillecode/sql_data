'''Find common word Function With count using Dictionary data structure'''
import os
import string
from pprint import pprint
from operator import itemgetter

print(os.getcwd()) #this gets the working directory
os.chdir('/Users/shaq/Desktop/archive/sql_data/data')#this changes the working directory
print(os.getcwd()) # This show changes

text="""
Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.
Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs. These might be considered part of the programming process, but often the term software development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code. Software engineering combines engineering techniques with software development practices. Reverse engineering is a related process used by designers, analysts and programmers to understand and re-create/re-implement
"""

def find_common_word(text):
    '''Finds Common word'''

    #so i want to filter out by the word list
    with open('function_words.txt') as fin:
        word_list = list(map(lambda x:x.strip(), fin.readlines()))
        # for line in f.readlines():
        #     line = line.strip()
        #     print(line)

    text = text.translate(str.maketrans('', '', string.punctuation ))
    the_list = text.lower().split()
    the_dict = {}
    for word in the_list:
        if word not in word_list:
            if word not in the_dict:
                the_dict[word] = 0
            the_dict[word] += 1
    common_word = [f'"{k}" is the most common word. It appeared {v} times'
    for k,v in the_dict.items() if v == max(the_dict.values())]
    pprint(sorted(the_dict.items(), key=itemgetter(1), reverse=True)[:5])
    pprint(common_word)

find_common_word(text)
