# Calculate the mean, median, and mode of the following data set:
numList = [88,89,90,93,84,86,88,91,88,87]

x = len(numList)
  
The_sum = sum(numList)
mean = The_sum / x
  
print("Mean / Average is: " + str(mean))

# Median
x = len(numList)
numList.sort()

if x % 2 == 0:
    median1 = numList[x//2]
    median2 = numList[x//2 - 1]
    median = (median1 + median2)/2
else:
    median = numList[x//2]
print("Median is: " + str(median))
print(numList)

# Mode
numlistlen = int(input("Please enter how many numbers you would like to compare: "))
mode = 0
for i in range(0,numlistlen):
    maxiumNum = max(numList)
    j = maxiumNum + 1
    count = [0]*j
for i in range(j):
    count[i]=0

for i in range(numlistlen):
    count[numList[i]] +=1

n = count[0] 
for i in range(1, j):
    if (count[i] > n):
        n = count[i] 
        mode = i 
print("This is the mode = "+str(mode)) 
print("This is the original list = "+str(numList))

import math
def isPrime(num):
    prime = False
    if num >= 2:
        
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
    return prime
    
for i in range(1000,1101):
    if isPrime(i):
        print(i)

import math
def isPrime(num):
    prime = False
    if num >= 2:
        #
        prime = True
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
    return prime
    
for i in range(1000,1101):
    if isPrime(i):
        sum_of_digits = sum([ int(x) for x in list(str(i))])
        print(i, sum_of_digits,isPrime(sum_of_digits))

#sum([ int(x) for x in list(str(i))])
digits = []
num = 1009 
total = 0
for i in list(str(num)):
    total += int(i)
print(total)


import random
students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
volunteers = []
n = 5
for i in range(n):
    picked = random.choice(students)
    print('{0} was picked'.format(picked))
    students.remove(picked)
    volunteers.append(picked)
    print(students)
print(f'I randomly picked the following students: {volunteers}')
print(f'Remaining students: {students}')

students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
def student_picker(x):
    return f"{random.sample(x, 5)} were chosen to volunteer"
print(student_picker(students))


students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
random.shuffle(students)
print(students[0:5])
