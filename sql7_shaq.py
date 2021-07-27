# Write a function that takes a string of chars, digits and symbols and returns a count of each one.

# i.e.

# str1 = "P@#yn26at^&i5ve" -> Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4

str1 = "P@#yn26at^&i5ve"

def splitString(str1):
 
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

from statistics import mode
# Part 1 Find Most common Letter in text
text = "Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs. These might be considered part of the programming process, but often the term software development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code. Software engineering combines engineering techniques with software development practices. Reverse engineering is a related process used by designers, analysts and programmers to understand and re-create/re-implement"

print("The original text is : " + str(text))
 
# getting all words
listcom1 = [wrd for sub in text for wrd in sub.split()]
 
# getting frequency
freq = mode(listcom1)
 
print("Letter with maximum frequency : " + str(freq))


# Part 2 Find Most common word in text list
text_list = ["Computer", "programming", "is", "the", "process", "of", "designing", "and", "building", "an", "executable", "computer", "program", "to", 'accomplish', 'a', 'specific', 'computing', 'result', 'or', 'to' 'perform', 'a', 'specific', 'task.', 'Programming', 'involves', 'tasks', 'such', 'as:', 'analysis', 'generating', 'algorithms', 'profiling', 'algorithms','accuracy', 'and', 'resource', 'consumption', 'and', 'the', 'implementation', 'of', 'algorithms', 'in', 'a', 'chosen', 'programming', 'language', 'commonly', 'referred', 'to', 'as', 'coding.', 'The', 'source', 'code', 'of', 'a', 'program', 'is', 'written', 'in', 'one', 'or', 'more', 'languages', 'that', 'are', 'intelligible', 'to', 'programmers', 'rather', 'than', 'machine code', 'which', 'is', 'directly', 'executed', 'by', 'the', 'central', 'processing', 'unit.', 'The', 'purpose', 'of', 'programming', 'is', 'to', 'find', 'a', 'sequence.', 'of', 'instructions', 'that', 'will', 'automate', 'the', 'performance', 'of', 'a', 'task', 'which', 'can', 'be', 'as', 'complex', 'as', 'an', 'operating,' 'system', 'on', 'a', 'computer,' 'often', 'for', 'solving', 'a', 'given', 'problem.', 'Proficient', 'programming', 'thus', 'often', 'requires', 'expertise', 'in', 'several', 'different subjects', 'including', 'knowledge', 'of', 'the', 'application', 'domain', 'specialized', 'algorithms', 'and', 'formal', 'logic.', 'Tasks', 'accompanying', 'and', 'related', 'to', 'programming', 'include:', 'testing', 'debugging', 'source', 'code', 'maintenance', 'implementation', 'of', 'build', 'systems', 'and', 'management', 'of', 'derived artifacts', 'such', 'as', 'the', 'machine', 'code', 'of', 'computer', 'programs.', 'These', 'might','be', 'considered', 'part', 'of', 'the', 'programming', 'process', 'but', 'often', 'the', 'term', 'software', 'development', 'is', 'used', 'for', 'this', 'larger', 'process', 'with', 'the', 'term', 'programming', 'implementation', 'or', 'coding', 'reserved', 'for', 'the', 'actual', 'writing', 'of', 'code.', 'Software', 'engineering', 'combines', 'engineering', 'techniques', 'with', 'software', 'development', 'practices.', 'Reverse', 'engineering', 'is', 'a', 'related', 'process', 'used', 'by', 'designers', 'analysts', 'and', 'programmers', 'to', 'understand', 'and', 're-create', 're-implement.']
 
 # getting all words
listcom2 = [wrd for sub in text_list for wrd in sub.split()]
 
# getting frequency
freq = mode(listcom2)
 
print("Word with maximum frequency : " + str(freq))


import mysql.connector
from dotenv import dotenv_values
config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

"""
Lists the number of customers in each country, sorted high to low
"""

query = """ 
SELECT COUNT(CustomerID), Country
FROM Customer
GROUP BY Country
ORDER BY COUNT(CustomerID) DESC;
"""

mycursor.execute(query)

for x in mycursor:
  print(x)
mydb.close()

import mysql.connector
from dotenv import dotenv_values
config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

query = """ 
SELECT COUNT(CustomerID), Country
FROM Customer
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
"""

mycursor.execute(query)

for x in mycursor:
  print(x)
mydb.close()

import mysql.connector
from dotenv import dotenv_values
config = dotenv_values("1.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password=' ',
  database='chinook'
)
mycursor = mydb.cursor()

"""
Lists the number of customers in each country. 
Only include countries with more than 5 customers
"""

query = """ 
SELECT City FROM Customer
UNION
SELECT City FROM Employee
ORDER BY City
"""

mycursor.execute(query)

for x in mycursor:
  print(x)
mydb.close()