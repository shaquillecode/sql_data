def is_it_a_palindrome_or_not(string = "racecar"):
    og_word = list(string)
    print(og_word)
    
    reverseword = og_word.copy()
    reverseword.reverse()
    print(reverseword)
    
    
    if((len(og_word)) %2 == 0 and (len(reverseword)) %2 == 0):
        print("Even lengthed Palindrome")
    else: 
        print("Odd lengthed Palindrome")

    if(og_word == reverseword ):
        return True
    else:
        return False 
    
The_answer = is_it_a_palindrome_or_not("racecar")  
The_answer2 = is_it_a_palindrome_or_not("tooth")   
print(The_answer)
print(The_answer2)
