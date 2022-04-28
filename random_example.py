"""Random"""
import math
import random

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
        sum_of_digits = sum([ int(x) for x in list(str(i))])
        print(i, sum_of_digits,isPrime(sum_of_digits))

#sum([ int(x) for x in list(str(i))])
digits = []
num = 1009
total = 0
for i in list(str(num)):
    total += int(i)
print(total)

elementary_school_students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']
volunteers = []
n = 5
for i in range(n):
    picked = random.choice(elementary_school_students)
    print('{0} was picked'.format(picked))
    elementary_school_students.remove(picked)
    volunteers.append(picked)

print(f'I randomly picked the following students: {volunteers}')
print(f'Remaining students: {elementary_school_students}')
print('==='*35)

middle_school_students = ['Hindy','Shaniqua','Kevin','Sade','Charly','Karen','Shaquille','Mary-Ann','Billy','Bob','Mary-kate','Sue']
def student_picker(x):
    return f"{random.sample(x, 5)} were chosen to volunteer"
print(student_picker(middle_school_students))
print('==='*35)

high_school_students = ['Sue','Candace','Damian','Christy','Shaq','Brittney','Dwight','Sue-Ann','Gary','Jr','Jeremy','Kayla']
random.shuffle(high_school_students)
print(high_school_students[0:5])
