# A cesear cipher is a simple cipher that shifts four letters to the left. Julius Cesear used to use this cipher for his personal correspondence in ancient rome.



original = "THE-QUICK-BROWN-FOX-JUMPS-OVER-THE-LAZY-DOG"

a = ""
LETTERS = 26
def ceaser_cipher(C, CI):
   b = ""
   for i in C:
      if(i.isupper()):
         a = ord(i)
         a = a + CI
         if a > ord('Z'):
            a = a - LETTERS
         elif a < ord('A'):
            a = a + LETTERS
         b = b + chr(a)
      else:
         b = b + "-"
   return b

print(ceaser_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 23))
print(original)